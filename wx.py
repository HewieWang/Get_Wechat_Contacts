import uiautomation as auto
import csv,codecs

result = []
wechat_str=""

wechatWindow = auto.WindowControl(searchDepth=1, Name="微信", ClassName='WeChatMainWndForPC')
wechatWindow.SetActive()
txl_btn = wechatWindow.ButtonControl(Name='通讯录')
txl_btn.Click()
contacts=wechatWindow.ListControl(Name="联系人")
contacts.GetChildren()[6].Click()
send_msg=wechatWindow.ButtonControl(Name='发消息')
detail=send_msg.GetParentControl()
result.append(["昵称", "签名", "备注", "地区", "微信号"])

for i in range(1,5000):
    try:
        nickname=detail.GetChildren()[0].GetChildren()[0].GetChildren()[0].GetChildren()[0].Name
        # sign=""
        sign=detail.GetChildren()[0].GetChildren()[0].GetChildren()[1].Name
        remark=detail.GetChildren()[2].GetChildren()[0].GetChildren()[1].Name
        address=detail.GetChildren()[2].GetChildren()[1].GetChildren()[1].Name
        wechat=detail.GetChildren()[2].GetChildren()[2].GetChildren()[1].Name

        if wechat+"," in wechat_str:
            break
            pass
        # print([nickname, sign, remark,address, wechat])
        wechat_str+=wechat+","
        result.append([nickname, sign, remark,address, wechat])
        contacts.SendKeys("{DOWN}")
        pass
    except Exception as e:
        if e.args[0]=="list index out of range":
            nickname=detail.GetChildren()[0].GetChildren()[0].GetChildren()[0].GetChildren()[0].Name
            sign=""
            remark=detail.GetChildren()[2].GetChildren()[0].GetChildren()[1].Name
            address=detail.GetChildren()[2].GetChildren()[1].GetChildren()[1].Name
            wechat=detail.GetChildren()[2].GetChildren()[2].GetChildren()[1].Name
            if wechat+"," in wechat_str:
                break
                pass
            wechat_str+=wechat+","
            result.append([nickname, sign, remark,address, wechat])
            pass
        # print(e.args[0])
        pass
        contacts.SendKeys("{DOWN}")
        continue
    pass

file_csv = codecs.open("通讯录.csv",'w+','utf-8-sig')
writer = csv.writer(file_csv, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
for data in result:
    writer.writerow(data)
print("保存文件成功，处理结束")
