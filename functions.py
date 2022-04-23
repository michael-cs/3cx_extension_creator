import random
import string
#data=[Number,FirstName,LastName,EmailAddress,MobileNumber,AuthID,AuthPassword,WebMeetingFriendlyName,WebMeetingPrivateRoom,ClickToCall,ClickToCallFriendlyName,WebMeetingAcceptReject,EnableVoicemail,VMNoPin,VMPlayCallerID,PIN,VMPlayMsgDateTime,VMEmailOptions,QueueStatus,OutboundCallerID,SIPID,DeliverAudio,SupportReinvite,SupportReplaces,EnableSRTP,ManagementAccess,ReporterAccess,WallboardAccess,TurnOffMyPhone,HideFWrules,CanSeeRecordings,CanDeleteRecordings,RecordCalls,CallScreening,EmailMissedCalls,Disabled,DisableExternalCalls,AllowLanOnly,BlockRemoteTunnel,PinProtect,MAC_0,InterfaceIP_0,UseTunnel,DND,UseCTI,StartupScreen,HotelModuleAccess,DontShowExtInPHBK,DeskphoneWebPass,SrvcAccessPwd,VoipAdmin,SysAdmin,SecureSIP,PhoneModel14,PhoneTemplate14,CustomTemplate,PhoneSettings,AllowAllRecordings,PushExtension,Integration,AllowOwnRecordings,RecordExternalCallsOnly,DID,SMS,PhoneSysAdmin]
def pass_random ():
    ascii_options = string.ascii_letters
    ascii_lower=string.ascii_lowercase
    ascii_upper=string.ascii_uppercase
    number_options = string.digits
    options=ascii_options + number_options + ascii_lower +ascii_upper
    password=''

    for i in range(0,10):
        if i == 7:
            digit = random.choice(number_options)
            password+=digit
        elif i == 3:
            digit = random.choice(ascii_lower)
            password+=digit
        elif i == 2:
            digit = random.choice(ascii_upper)
            password+=digit
        else:
            digit=random.choice(options)
            password+=digit
    return password

def meeting_random ():
    #ascii_lower=string.ascii_lowercase
    number_options = string.digits
    options=number_options
    meet='webmeeting'+''
    for i in range (0,6):
        digit=random.choice(options)
        meet+=digit
    return meet

def pin_random():
    number_options=string.digits
    pin=''
    for i in range(0,4):
        digit=random.choice(number_options)
        pin+=digit
    return pin
#response = pin_random()
#print(response)



    
