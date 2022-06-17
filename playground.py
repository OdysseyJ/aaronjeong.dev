from abc import *


# 고객에게 지급될때 쿠폰이라는 타입으로 지급된다고 가정
class GiveType(metaclass=ABCMeta):
    @abstractmethod
    def give(self):
        raise NotImplementedError()


class GiveInApp(GiveType):
    def give(self):
        print("앱 내에서 리스트에 보여주기")


class GiveInTextMessage(GiveType):
    def give(self):
        print("문자로 전송")


####


class Uploader(metaclass=ABCMeta):
    @abstractmethod
    def upload(self):
        raise NotImplementedError()


class PointUploader(Uploader):
    def upload(self):
        print("포인트 파일 업로드")


class VoucherUploader(Uploader):
    def upload(self):
        print("바우처 파일 업로드")


###


class Coupon(metaclass=ABCMeta):
    uploader: Uploader
    give_type: GiveType

    @property
    @abstractmethod
    def amount(self):
        raise NotImplementedError()

    def upload(self):
        self.uploader.upload()

    def give(self):
        self.give_type.give()


class NaverCoupon(Coupon):
    def __init__(self):
        self.uploader = PointUploader()
        self.give_type = GiveInApp()


class HappyMoneyCoupon(Coupon):
    def __init__(self):
        self.uploader = VoucherUploader()
        self.give_type = GiveInTextMessage()


class CultureLandCoupon(Coupon):
    def __init__(self):
        self.uploader = VoucherUploader()
        self.give_type = GiveInTextMessage()


class HappyLandCoupon(Coupon):
    def __init__(self):
        self.uploader = VoucherUploader()
        self.give_type = GiveInTextMessage()


def problem_solve_and_give_coupon(self, problem):
    problem.solve()
    NaverCoupon().give()


def upload_by_slack(self):
    file_name = "naver_20220617.csv"
    indicator = file_name.split("_")[0]
    coupon_map = {
        "naver": NaverCoupon,
        "happy": HappyMoneyCoupon
    }
    coupon: Coupon = coupon_map[indicator]()
    coupon.upload()

