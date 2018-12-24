# coding=utf-8
# --author='fangfang'

from package.interface.ycd360_put_assert import ycd360_assert

ya = ycd360_assert()

orgLoanId = "SDTJ2018121600568113"

# ya.accountStatusQuery("18514593476", "420101199404166850",  "刘强文", "6212461600000501696")
# ya.assetPush(orgLoanId, "106", "18514593476", "420101199404166850", "刘强文", "6212461600000501696")
# ya.assetConfirm(orgLoanId)
# ya.assetRevoke(orgLoanId)
ya.accountStatusQuery("13296747005", "91210211MA0UREXG02", "大连濠林汽车经纪服务有限公司", "6212461600001001639")
# ya.assetStatusQuery(orgLoanId)
