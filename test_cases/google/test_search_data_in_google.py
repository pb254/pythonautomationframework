from app_lib.google.ui.pages.common import Common
import  time
import six


def test_search_data_in_google():

    common = Common()

    common.open_google_website("http://cbseresults.nic.in/cbseresults_cms/Public/Home.aspx")

    common.refresh_until_element_found()

    six.print_ (time.sleep(5))