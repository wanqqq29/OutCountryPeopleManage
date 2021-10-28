<template>
  <div class="q-pa-md">
    <q-table
      title="出国人员信息导出"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :visible-columns="visibleColumns"
      :rows-per-page-options="[10, 20]"
      ref="tb"
      :filter="filter"
      :loading="loading"
      no-data-label="I didn't find anything for you"
      no-results-label="The filter didn't uncover any results"
    >
      <template v-slot:top="props">
        <q-space />
        <q-input
          borderless
          dense
          debounce="300"
          v-model="filter"
          placeholder="Search"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
        <q-select
          v-model="visibleColumns"
          multiple
          outlined
          dense
          options-dense
          :display-value="$q.lang.table.columns"
          emit-value
          map-options
          :options="columns"
          option-value="name"
          options-cover
          style="min-width: 150px"
        />
        <q-btn
          flat
          round
          dense
          :icon="props.inFullscreen ? 'fullscreen_exit' : 'fullscreen'"
          @click="props.toggleFullscreen"
          class="q-ml-md"
        />
        <q-btn
          color="primary"
          icon-right="archive"
          label="导出"
          no-caps
          @click="exportTable"
        />
      </template>

      <template v-slot:no-data="{ icon, message, filter }">
        <div class="full-width row flex-center text-accent q-gutter-sm">
          <q-icon size="2em" name="sentiment_dissatisfied" />
          <span> Well this is sad... {{ message }} </span>
          <q-icon size="2em" :name="filter ? 'filter_b_and_w' : icon" />
        </div>
      </template>

      <template v-slot:loading>
        <q-inner-loading showing color="primary" />
      </template>
    </q-table>
  </div>
</template>

<script>
import { ref, onMounted, reactive } from "vue";
import { exportFile, useQuasar } from "quasar";
import { api } from "boot/axios";

function wrapCsvValue(val, formatFn) {
  let formatted = formatFn !== void 0 ? formatFn(val) : val;

  formatted =
    formatted === void 0 || formatted === null ? "" : String(formatted);

  formatted = formatted.split('"').join('""');
  /**
   * Excel accepts \n and \r in strings, but some other CSV parsers do not
   * Uncomment the next two lines to escape new lines
   */
  // .split('\n').join('\\n')
  // .split('\r').join('\\r')

  return `"${formatted}"`;
}

export default {
  setup() {
    const columns = ref();

    const rows = ref();

    const $q = useQuasar();

    const tb = ref(null);

    const visibleColumns = ref();

    const loading = ref(true);
    const filter = ref("");

    function exportTable() {
      // naive encoding to csv format
      const content = [columns.value.map((col) => wrapCsvValue(col.label))]
        .concat(
          tb.value.filteredSortedRows.map((row) =>
            columns.value
              .map((col) =>
                wrapCsvValue(
                  typeof col.field === "function"
                    ? col.field(row.value)
                    : row[col.field === void 0 ? col.name : col.field],
                  col.format
                )
              )
              .join(",")
          )
        )
        .join("\r\n");

      const status = exportFile(
        "table-export.csv",
        "\uFEFF" + content,
        "text/csv"
      );

      if (status !== true) {
        $q.notify({
          message: "Browser denied file download...",
          color: "negative",
          icon: "warning",
        });
      }
    }

    function loadData() {
      api.get("/CsR").then((response) => {
        var csrtoken = response.data;
        api
          .post(
            "/Sinfo/",
            { tk: csrtoken.jsdlak },
            { headers: { "X-CSRFToken": csrtoken.csrf_token } }
          )
          .then((response) => {
            columns.value = response.data.fields.Columns;
            rows.value = response.data.data;
            visibleColumns.value = response.data.fields.visibleColumns;
          })
          .catch((error) => {
            console.log(error);
            console.log("error");
          });
      });
    }

    onMounted(() => {
      loadData();
      setTimeout(() => {
        loading.value = false;
        console.log("loading", loading.value);
      }, 2000);
    });

    return {
      rows,
      tb,
      loading,
      loadData,
      columns,
      filter,
      exportTable,
      visibleColumns,
    };
  },
};
</script>
