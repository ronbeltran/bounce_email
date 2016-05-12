BOUNCE_EMAIL1 = """
Delivered-To: rbbeltran.09@gmail.com
Received: by 10.64.103.70 with SMTP id fu6csp65616ieb;
        Fri, 25 May 2012 06:48:50 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=googlemail.com; s=20120113;
        h=mime-version:from:to:x-failed-recipients:subject:message-id:date
         :content-type:content-transfer-encoding;
        bh=Q4Z3IVyZX8XJ2dG8jpKRLKyWwOQHpXzLkXlK+wZG8Zo=;
        b=dSu/VAXwSRy3IXmS/dgk4fdmoAv5YXjYoiTptlY6HRS+XqK28oEfworYluI7tHhtJN
         rKo91Qh/tIUEsCyuHMmRmjuG7KOaN6dSH1IVsY/xEnX7/s+BfCZ7ATZYdRD6ZW8Ve7/h
         RBGAwf+dRqrhIPSWST0XAm0G4Ukq7Cqjdh1Qty0DyOGW9yANn+cnQiAz5vTZ3ArbArhj
         5TBe6cnitqi8GfeAL6Mgm+IlU8w70CYLPBwabKzQORYIXSgYqzKrutGnFeJ9wpCwa/dg
         1Q5IH1ye04A0RKFR/f1L6L/eWkw3lUXhTYYOyFSNmOROhDd9NJwy95lt/B0ForZ7b0Wf
         0++w==
Received: by 10.50.196.232 with SMTP id ip8mr2750533igc.50.1337953729968;
        Fri, 25 May 2012 06:48:49 -0700 (PDT)
MIME-Version: 1.0
Return-Path: <>
Received: by 10.50.196.232 with SMTP id ip8mr3686795igc.50; Fri, 25 May 2012
 06:48:49 -0700 (PDT)
From: Mail Delivery Subsystem <mailer-daemon@googlemail.com>
To: rbbeltran.09@gmail.com
X-Failed-Recipients: rbbeltran20032003@yahoo.com
Subject: Delivery Status Notification (Failure)
Message-ID: <14dae9341241ccf67f04c0dca048@google.com>
Date: Fri, 25 May 2012 13:48:49 +0000
Content-Type: text/plain; charset=ISO-8859-1
Content-Transfer-Encoding: quoted-printable

Delivery to the following recipient failed permanently:

     rbbeltran20032003@yahoo.com

Technical details of permanent failure:=20
Google tried to deliver your message, but it was rejected by the recipient =
domain. We recommend contacting the other email provider for further inform=
ation about the cause of this error. The error that the other server return=
ed was: 554 554 delivery error: dd Sorry your message to rbbeltran20032003@=
yahoo.com cannot be delivered. This account has been disabled or discontinu=
ed [#102]. - mta1087.mail.gq1.yahoo.com (state 17).

----- Original message -----

DKIM-Signature: v=3D1; a=3Drsa-sha256; c=3Drelaxed/relaxed;
        d=3Dgmail.com; s=3D20120113;
        h=3Dmime-version:date:message-id:subject:from:to:content-type;
        bh=3DHxY2UoRxaOOZf+06PFvxq4ypSholfrmxvEx3TqDRQ54=3D;
        b=3DqCHn/NXK1Mw0p2zOQeBSDz4qtqFvPUFXlRogtYjZyCrVkvIOaDUvfgVcP0++TVm=
Po9
         heoUT/i96wYkNHNCLTkOpHywRd3MBpQ6hJAknqiIZz57iOkIWRQsEJVXNrgUCB6Uad=
B1
         6wzy1a6M1fD9RUWh0j3mjyG89rQNpjp1gaeBsGCC6FCsDukOBrHLJe5gXtRYXR/iLz=
E9
         SUngqb12u8rykQVAY+HopYDCViyW+/t47QW2s4toRy3MXAufeWbTkscpd0wOyRYrkO=
Ib
         XquRojFtkZBUvLC2qC4E+exmegR6R/23jPntsTknuhcZ3ksa+KOqhRS9D7wM8VB88X=
Yn
         UbAg=3D=3D
MIME-Version: 1.0
Received: by 10.50.196.232 with SMTP id ip8mr2750475igc.50.1337953729354; F=
ri,
 25 May 2012 06:48:49 -0700 (PDT)
Received: by 10.64.103.70 with HTTP; Fri, 25 May 2012 06:48:49 -0700 (PDT)
Date: Fri, 25 May 2012 21:48:49 +0800
Message-ID: <CACwALKX+rgqb0Ehua-djc4X9fCjLo5SVOwRcmSJ1Wnt0nS26EA@mail.gmail=
.com>
Subject: test
From: Ronnie Beltran <rbbeltran.09@gmail.com>
To: rbbeltran20032003@yahoo.com
Content-Type: multipart/alternative; boundary=3D14dae9341241c39ac604c0dca02=
d

test
"""

BOUNCE_EMAIL2 = """
Delivered-To: rbbeltran.09@gmail.com
Received: by 10.64.240.18 with SMTP id vw18csp625391iec;
        Wed, 11 May 2016 23:04:09 -0700 (PDT)
X-Received: by 10.36.155.132 with SMTP id o126mr7675415itd.95.1463033048992;
        Wed, 11 May 2016 23:04:08 -0700 (PDT)
Return-Path: <>
Received: from mail-ig0-f200.google.com (mail-ig0-f200.google.com. [209.85.213.200])
        by mx.google.com with ESMTPS id w98si7597847ioe.0.2016.05.11.23.04.08
        for <rbbeltran.09@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);
        Wed, 11 May 2016 23:04:08 -0700 (PDT)
Received-SPF: pass (google.com: best guess record for domain of postmaster@mail-ig0-f200.google.com designates 209.85.213.200 as permitted sender) client-ip=209.85.213.200;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@googlemail.com;
       spf=pass (google.com: best guess record for domain of postmaster@mail-ig0-f200.google.com designates 209.85.213.200 as permitted sender) smtp.helo=mail-ig0-f200.google.com;
       dmarc=pass (p=QUARANTINE dis=NONE) header.from=googlemail.com
Received: by mail-ig0-f200.google.com with SMTP id kj7so71805019igb.3
        for <rbbeltran.09@gmail.com>; Wed, 11 May 2016 23:04:08 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=googlemail.com; s=20120113;
        h=mime-version:from:to:subject:message-id:date;
        bh=qsHY1UqoXLX7R2yyvDHyINuGC4Nf4zJ4eCxWQQFh7J0=;
        b=sfy2A21gMhOXq10VGNhnjwjnbytFDFKrgWGy4pQYrwrTnRAiKOO2BH2yj/Uco4FZUI
         Zz45wuzv7+xgqywLOau9jheFY0QtkXgk6zYgEHExuzk1HDIikyuMXHP9j6XtM9OVUljX
         lQcQOPy9PP/1aJU9ndb+LSEIiisD2WBQ5AIPOb9wvGcIcTZJa6VMlvub2N/jbJJhLIgD
         jjdtedpDXimjid7iFRbzfEX5G0ILFlOuMDPsMl9a5bN4a/YWbShSBDbDFV13iyFUr5ZV
         8igGlz0MQOuqClr/33Jy1e6lv1R5t1IILCEuVzMd43zoR+ORKOIZhYuRLGDMJGQ+21eM
         RCfQ==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20130820;
        h=x-gm-message-state:mime-version:from:to:subject:message-id:date;
        bh=qsHY1UqoXLX7R2yyvDHyINuGC4Nf4zJ4eCxWQQFh7J0=;
        b=A66tDPvSR0G2PzvOdLERBc0dbPz+fW7GPY/gK26TZZXjaIaQHV34KF6yyVNmELf7nw
         ab5alo2m40myAefbpRRoESzEKpT7MQ+Wrk9aGdsYotFomoFPnVWNX1kXmCrz9pLgi+oN
         0bBnGb/Mh0FJVLaqmkDu0Lh5jy6hCneU9zFDSWkRtDUiU4OsfPib9WAOnqhQSOLia7mZ
         OSFREJXFIyGvzAOE9DaX5veoTENuPZUe2EifVajV9Xt/5JaUCdWnHoZald8StLCfGXb0
         qjQ9rdSfO6W6EyKyDZLL3RaUydhKbo59bViM4xYXwranq+6acJyUKswYNBOeC2XN4kQd
         yYWQ==
X-Gm-Message-State: AOPr4FUn+uDQ3nACernEVISnnOFAHPSimUWpKLcWLOXX7Y2VS0ctBVEYWmYD9mgCjt4vxaRgZNWaKbKI5F7P3dK+bTCUJbbeRg==
X-Received: by 10.107.7.170 with SMTP id g42mr6102816ioi.81.1463033048812;
        Wed, 11 May 2016 23:04:08 -0700 (PDT)
MIME-Version: 1.0
Return-Path: <>
Received: by 10.107.7.170 with SMTP id g42mr6186369ioi.81; Wed, 11 May 2016
 23:04:08 -0700 (PDT)
From: Mail Delivery Subsystem <mailer-daemon@googlemail.com>
To: rbbeltran.09@gmail.com
X-Failed-Recipients: card@hsbc.com.ph
Subject: Delivery Status Notification (Failure)
Message-ID: <001a113f27ce2b4a3d05329eedc3@google.com>
Date: Thu, 12 May 2016 06:04:08 +0000
Content-Type: text/plain; charset=UTF-8

Delivery to the following recipient failed permanently:

     card@hsbc.com.ph

Technical details of permanent failure: 
Google tried to deliver your message, but it was rejected by the server for the recipient domain hsbc.com.ph by smtp1.hsbc.com.hk. [203.112.90.3].

The error that the other server returned was:
550 Denied by policy


----- Original message -----

DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20120113;
        h=mime-version:date:message-id:subject:from:to;
        bh=UakhYMmj34AvR9r3aZyjypRCk/r7oVzDOHmQYUj9uN8=;
        b=va/+7nJ+/ePoR21SOLKV8XSWqIrDA9dpwSj4QWCAqIYBclYs/MGzRVyIt5aXX5eL3k
         HWljgBtg586ZLWqQUdXdy8I698BIsUsQM7RlJ7H4i/A1SC1h86NIN7g1v0tEoGjEmSJn
         DTWmDaMUJoSbkNNl3lbHzYP+xqRyySW2Q+bnYHurs2GtFplTcjV+mMFbQ3nyyUwoZhmw
         WuYiyd6SQlKxYk3wqCYmRT2xUtjJXEk+Ow73JVECYoYIS3sn0r9kGZT0TBjxOGHgzj2/
         l0mnXG1UoqJzqpjMqi5WoUdHOksZUNoA6/E6v4lwIWpCeG/jAq/czw6RrlhQgdpv1aMg
         K5KA==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20130820;
        h=x-gm-message-state:mime-version:date:message-id:subject:from:to;
        bh=UakhYMmj34AvR9r3aZyjypRCk/r7oVzDOHmQYUj9uN8=;
        b=lcw2r1UZjmFpboO5XieT5SORFgWk6ObS3I/AooQ/7iFcJrC3jynH4ij5a3+7fIVFpV
         FlSi3F8Co/bNuQ9zBLHxEAvCkd6myR5WUbwzH1ClJdByBuh2EC2h3C56gIU1cfV7Dii1
         aSAAMekki6h9dJ9lxEUpJ0/0JTmMf9EZZUUAaIMSPgJQlpldezEBYagje5QO65HoTIdr
         p2oAhk/PdR0fMFkSBN35ubBLszO2EvK3rOHUZWLBJsfNzAUY3e1BVQjvgfhLxn6+bh3s
         BR9l3bVD5DF1hTwDt7nL1OHlKawEvwuXDEJKc/1P+allilE4scM+dlZfN6b3XPv3KdRB
         34Bg==
X-Gm-Message-State: AOPr4FXkSe1OCjzsZ/LPm3521MBDRoiY3wfUw6ElE8IyK+yNEDcV9B1qsABs30KH7ZqBG0liRdVJO88hi/K5wA==
MIME-Version: 1.0
X-Received: by 10.107.7.170 with SMTP id g42mr6102675ioi.81.1463033046052;
 Wed, 11 May 2016 23:04:06 -0700 (PDT)
Received: by 10.64.98.230 with HTTP; Wed, 11 May 2016 23:04:06 -0700 (PDT)
Date: Thu, 12 May 2016 14:04:06 +0800
Message-ID: <CACwALKW8d1kMAPhyvu66DPzKtx-8kzdZnXXwv3+Z5yYzsiFmUQ@mail.gmail.com>
Subject: TEST: This email should bounce
From: Ronnie Beltran <rbbeltran.09@gmail.com>
To: card@hsbc.com.ph
Content-Type: multipart/alternative; boundary=001a113f27ce01391305329eed4b

Hey HSBC, just checking the email address availability.
"""

NORMAL_EMAIL1 = """
MIME-Version: 1.0
Received: by 10.64.27.198 with HTTP; Wed, 20 Apr 2016 20:28:34 -0700 (PDT)
In-Reply-To: <CACQ2dkVTnf_mFRZ2n0eebDxKDQTZNCJ8noJt0zvcgUTXcucJNg@mail.gmail.com>
References: <CACQ2dkVTnf_mFRZ2n0eebDxKDQTZNCJ8noJt0zvcgUTXcucJNg@mail.gmail.com>
Date: Thu, 21 Apr 2016 11:28:34 +0800
Delivered-To: rbbeltran.09@gmail.com
Message-ID: <CACwALKX37AFaN2eNEitbc-mrwXi=q+QCf1c6vTmncTh7UMuiwQ@mail.gmail.com>
Subject: Re: TEST Salesforce Email Tracking
From: Ronnie Beltran <rbbeltran.09@gmail.com>
To: Ronnie Beltran <ronnie@collabspot.com>
Content-Type: multipart/alternative; boundary=e89a8f3ba2d926983a0530f64eb7

--e89a8f3ba2d926983a0530f64eb7
Content-Type: text/plain; charset=UTF-8

gotcha!

On Thu, Apr 21, 2016 at 11:27 AM, Ronnie Beltran <ronnie@collabspot.com>
wrote:

> https://collabspot-dev-ed.my.salesforce.com
> <https://wmp-highrise-plugin-2.appspot.com/r/8b047e111c93294a2931a8db8a4ec0dd?d=https%3A%2F%2Fcollabspot-dev-ed.my.salesforce.com>
>
> --
> *Ronnie Beltran*
> *Developer at Collabspot*
>

--e89a8f3ba2d926983a0530f64eb7
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr">gotcha!</div><div class=3D"gmail_extra"><br><div class=3D"=
gmail_quote">On Thu, Apr 21, 2016 at 11:27 AM, Ronnie Beltran <span dir=3D"=
ltr">&lt;<a href=3D"mailto:ronnie@collabspot.com" target=3D"_blank">ronnie@=
collabspot.com</a>&gt;</span> wrote:<br><blockquote class=3D"gmail_quote" s=
tyle=3D"margin:0 0 0 .8ex;border-left:1px #ccc solid;padding-left:1ex"><div=
 dir=3D"ltr"><a href=3D"https://wmp-highrise-plugin-2.appspot.com/r/8b047e1=
11c93294a2931a8db8a4ec0dd?d=3Dhttps%3A%2F%2Fcollabspot-dev-ed.my.salesforce=
.com" target=3D"_blank">https://collabspot-dev-ed.my.salesforce.com</a><spa=
n class=3D"HOEnZb"><font color=3D"#888888"><br clear=3D"all"><div><br></div=
>-- <br><div><div dir=3D"ltr"><b>Ronnie Beltran</b><div><b>Developer at Col=
labspot</b></div></div></div>
<img src=3D"https://wmp-highrise-plugin-2.appspot.com/t/8b047e111c93294a293=
1a8db8a4ec0dd/empty.gif" style=3D"border:0;width:1px;min-height:1px"></font=
></span></div>
</blockquote></div><br></div>

--e89a8f3ba2d926983a0530f64eb7--
"""
