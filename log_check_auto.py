

# with 문으로 파일 전체 읽는거 말고 한 줄씩 읽는거 수행 해보기

f = open("202.txt", 'r', encoding='utf-8')
lines = f.readlines()
camera_opened_cnt = 0
upload_status_cnt = 0
hostname_issue_cnt = 0
timed_out_cnt = 0
camera_opend_list = []
upload_status_list = []
hostname_issue_list = []
timed_out_list = []

'''
2020-12-17 14:32:05.189==RecorderService:Camera.opened
2020-12-17 17:41:37.294==ihp.Upload:statusLine=HTTP/1.1 201 Created
2020-12-17 14:33:45.494==ihp.Upload:httpUpload Throwable=Unable to resolve host "api.inhandplus.com": No address associated with hostname
2020-12-17 18:24:03.367==ihp.Upload:httpUpload Throwable=Connection has been shut down

2020-12-17 18:24:03.367==ihp.Upload:httpUpload Throwable=Connect to api.inhandplus.com:80 timed out
2020-12-23 14:11:24.788==ihp.Upload:statusLine=HTTP/1.1 502 Bad Gateway

'''
for line in lines:
    if 'Camera.opened' in line:
        camera_opened_cnt += 1
        print(line)
        camera_opend_list.append(line)
    elif 'Upload:statusLine=HTTP/1.1' in line:
        upload_status_cnt += 1
        print(line)
        upload_status_list.append(line)
    elif 'No address associated with hostname' in line:
        hostname_issue_cnt += 1
        print(line)
        hostname_issue_list.append(line)
    elif 'api.inhandplus.com:80 timed out' in line:
        print(line)
        timed_out_cnt += 1
        timed_out_list.append(line)
    else:
        pass

print("camera_opened은 {}회 발생하였고 해당 로그는".format(
    camera_opened_cnt), camera_opend_list)
print('====================================================================================================================')
print("Upload:statusLine=HTTP/1.1 201 Created는 {}회 발생하였고 해당 로그는".format(
    upload_status_cnt), upload_status_list)
print('====================================================================================================================')
print("No address associated with hostname은 {}회 발생하였고 해당 로그는".format(
    hostname_issue_cnt), hostname_issue_list)
print('====================================================================================================================')
print("timed out은 {}회 발생하였고 해당 로그는".format(timed_out_cnt), timed_out_list)
f.close()
