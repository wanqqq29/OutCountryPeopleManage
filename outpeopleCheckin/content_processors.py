import time

from outpeopleCheckin.models import Tinfo, Sinfo, Cinfo, SCinfo


def detailid(request):
    if request.user.is_authenticated:
        if Tinfo.objects.filter(applicant=request.user).exists():
            deatile = Tinfo.objects.filter(applicant=request.user).first().id
            Cflag = Cinfo.objects.filter(applicant=request.user).exists()
            if Cflag:
                C = True
            elif not Cflag:
                C = False
            return {
                'detailid': deatile, 'group': True, 'C': C
            }
        elif Sinfo.objects.filter(applicant=request.user).exists():
            deatile = Sinfo.objects.filter(applicant=request.user).first().id
            Cflag = SCinfo.objects.filter(applicant=request.user).exists()
            if Cflag:
                C = True
            elif not Cflag:
                C = False
            return {
                'detailid': deatile, 'group': False, 'C': C
            }
        else:
            return {
                'detailid': ''
            }
    else:
        return {
            'detailid': ''
        }
