from django.contrib.auth import get_user_model
from django.conf import settings
from .custom_auth import check_if_user


UserModel = get_user_model()

class UserBackend(object):
    def authenticate(self, username=None, password=None):
        if check_if_user(username, password): # OO커뮤니티 사이트 인증에 성공한 경우
            try: # 유저가 있는 경우
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist: # 유저 정보가 없지만 인증 통과시 user 생성
                user = UserModel(username=username)
                user.is_staff = False
                user.is_superuser = False
                user.save()
                # 여기서는 user.password를 저장하는 의미가 없음.(장고가 관리 못함)
            return user

    #def user_can_authenticate(self, user):
    #    is_active = getattr(user, 'is_active', None) # 유저가 활성화 되었는지
    #    return is_active or is_active is None # 유저가 없는 경우 is_active는 None이므로 True

    def get_user(self, user_id):
        try:
            #return UserModel.objects.get(pk=user_id) # 유저를 pk로 가져온다
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None