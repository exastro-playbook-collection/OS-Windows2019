Ansible Role: OS-Windows2019/WIN_PrivateSetting/OS_build
=======================================================
# Description
本ロールは、Windows Server 2019に関するプライバシー設定についての情報の設定を行います。

# Supports
- 管理マシン(Ansibleサーバ)
  * Linux系OS（RHEL7）
  * Ansible バージョン 2.7 以上 (動作確認バージョン 2.7, 2.9)
  * Python バージョン 3.x  (動作確認バージョン 3.6)
- 管理対象マシン
  * Windows Server 2019

# Requirements
- 管理マシン(Ansibleサーバ)
  * Ansibleサーバは管理対象マシンへPowershell接続できる必要があります。
- 管理対象マシン
  * Windows Server 2019
  * Powershell3.0+

# Dependencies

本ロールでは、他のロールは必要ありません。
ただし、本READMEに書かれている「エビデンスを取得する場合」の手順を行う場合は、
OS-Windows2019/WIN_PrivateSetting/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_PrivateSetting` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`location` | 「設定」「プライバシー」「アプリのアクセス許可」「位置情報」の「デバイスの位置情報 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`webcam` | 「設定」「プライバシー」「アプリのアクセス許可」「カメラ」の「デバイスのカメラ アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`microphone` | 「設定」「プライバシー」「アプリのアクセス許可」「マイク」の「デバイスのマイク アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`userNotificationListener` | 「設定」「プライバシー」「アプリのアクセス許可」「通知」の「デバイスの通知 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`userAccountInformation` | 「設定」「プライバシー」「アプリのアクセス許可」「アカウント情報」の「デバイスのアカウント情報 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`contacts` | 「設定」「プライバシー」「アプリのアクセス許可」「連絡先」の「デバイスの連絡先 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`appointments` | 「設定」「プライバシー」「アプリのアクセス許可」「カレンダー」の「デバイスのカレンダー アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`phoneCallHistory` | 「設定」「プライバシー」「アプリのアクセス許可」「通話履歴」の「デバイスの通話履歴 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`email` | 「設定」「プライバシー」「アプリのアクセス許可」「メール」の「デバイスのメール アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`userDataTasks` | 「設定」「プライバシー」「アプリのアクセス許可」「タスク」の「デバイスのタスク アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`chat` | 「設定」「プライバシー」「アプリのアクセス許可」「メッセージング」の「デバイスのメッセージング アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`radios` | 「設定」「プライバシー」「アプリのアクセス許可」「無線」の「デバイスの無線 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`bluetoothSync` | 「設定」「プライバシー」「アプリのアクセス許可」「他のデバイス」の「ペアリングされていないデバイスとの通信許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`appDiagnostics` | 「設定」「プライバシー」「アプリのアクセス許可」「アプリの診断」の「デバイスのアプリの診断 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`documentsLibrary` | 「設定」「プライバシー」「アプリのアクセス許可」「ドキュメント」の「デバイスのドキュメントライブラリ アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`picturesLibrary` | 「設定」「プライバシー」「アプリのアクセス許可」「ピクチャ」の「デバイスのピクチャライブラリ アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`videosLibrary` | 「設定」「プライバシー」「アプリのアクセス許可」「ビデオ」の「デバイスのビデオライブラリ アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`broadFileSystemAccess` | 「設定」「プライバシー」「アプリのアクセス許可」「ファイルシステム」の「デバイスのファイルシステム アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 

### Example
~~~
VAR_WIN_PrivateSetting:
  appDiagnostics: Allow
  appointments: Allow
  bluetoothSync: Allow
  broadFileSystemAccess: Allow
  chat: Allow
  contacts: Allow
  documentsLibrary: Allow
  email: Allow
  location: Allow
  microphone: Allow
  phoneCallHistory: Allow
  picturesLibrary: Allow
  radios: Allow
  userAccountInformation: Allow
  userDataTasks: Allow
  userNotificationListener: Allow
  videosLibrary: Allow
  webcam: Allow
~~~


## Optional Variables

特にありません。

# Usage

1. 本ロールを用いたPlaybookを作成します。
2. 変数を必要に応じて設定します。
3. Playbookを実行します。

# Example Playbook

## ■エビデンスを取得しない場合の呼び出す方法

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2019
    │         └── WIN_PrivateSetting/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_PrivateSetting.yml
    │                   │      build_Registry_present.yml
    │                   │      main.yml
    │                   └─ README.md
    └─ master_playbook.yml
~~~

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2019/WIN_PrivateSetting/OS_build
      VAR_WIN_PrivateSetting:
        appDiagnostics: Allow
        appointments: Allow
        bluetoothSync: Allow
        broadFileSystemAccess: Allow
        chat: Allow
        contacts: Allow
        documentsLibrary: Allow
        email: Allow
        location: Allow
        microphone: Allow
        phoneCallHistory: Allow
        picturesLibrary: Allow
        radios: Allow
        userAccountInformation: Allow
        userDataTasks: Allow
        userNotificationListener: Allow
        videosLibrary: Allow
        webcam: Allow
  strategy: free
~~~

- Running Playbook

~~~
> ansible-playbook master_playbook.yml
~~~

## ■エビデンスを取得する場合の呼び出す方法

エビデンスを収集する場合、以下のようなエビデンス収集用のPlaybookを作成してください。  

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2019/WIN_PrivateSetting/OS_build
      VAR_WIN_PrivateSetting:
        appDiagnostics: Allow
        appointments: Allow
        bluetoothSync: Allow
        broadFileSystemAccess: Allow
        chat: Allow
        contacts: Allow
        documentsLibrary: Allow
        email: Allow
        location: Allow
        microphone: Allow
        phoneCallHistory: Allow
        picturesLibrary: Allow
        radios: Allow
        userAccountInformation: Allow
        userDataTasks: Allow
        userNotificationListener: Allow
        videosLibrary: Allow
        webcam: Allow
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2019/WIN_PrivateSetting/OS_gathering
  strategy: free
~~~

- エビデンス収集結果一覧

エビデンス収集結果は、以下のように格納されます。
エビデンス収集結果の詳細は、OS_gatheringロールを確認してください。

~~~
#エビデンス構成
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_PrivateSetting/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_PrivateSetting.yml
~~~

# Remarks
-------

# License
-------

# Copyright
---------
Copyright (c) 2021 NEC Corporation

# Author Information
------------------
NEC Corporation
