#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

GroupNames={}    # GroupNames[""]=""
GroupNames["에이핑크"]="APink"
GroupNames["초롱"]="初珑"
GroupNames["보미"]="普美"
GroupNames["은지"]="恩地"
GroupNames["나은"]="娜恩"
GroupNames["하영"]="夏荣"
GroupNames["남주"]="南珠"

GroupNames["주니엘"]="Juniel"
GroupNames["씨크릿"]="Secret"
GroupNames["레드벨벳"]="Red Velvet"
GroupNames["비스트"]="BEAST"
GroupNames["에일리"]="Ailee"
GroupNames["걸스데이"]="Girl's Day "
GroupNames["소나무"]="SONAMOO"
GroupNames["달샤벳"]='Dal★Shabet'
GroupNames["여자친구"]='GFriend'
GroupNames["나인뮤지스"]='NineMuses'
GroupNames["포미닛"]="4minute"
GroupNames["티아라"]="T-ara"
GroupNames["씨스타"]="Sistar"
GroupNames["에이프릴"]="April"
GroupNames["이엑스아이디"]="EXID"
GroupNames["시크릿"]="Secret"
GroupNames["원더걸스"]="WonderGirls"
GroupNames["소녀시대"]="少女时代"
GroupNames["이지은"]="IU"
GroupNames["카라"]="Kara"
GroupNames["러블리즈"]="Lovelyz"
GroupNames["마마무"]="MAMAMOO"
GroupNames["헬로비너스"]="HelloVenus"
GroupNames["레인보우"]="Rainbow"
GroupNames["빅스"]="VIXX"
# OtherKrChar[""]=""
GroupNames["라붐"]="LABOUM"


OtherKrChar={}    #
#ProgramNames
OtherKrChar["뮤직뱅크"]='MusicBank'
OtherKrChar["음악중심"]="音乐中心"
OtherKrChar["비타민"]="维他命"
OtherKrChar["월호"]="月刊"
OtherKrChar["슈키라"]="kiss the radio"
OtherKrChar["엠카운트다운"]="M-Countdown"
OtherKrChar["컬투쇼"]="cultwo秀"
OtherKrChar["라디오"]="Radio"
OtherKrChar["마리텔"]="My Little Television"
OtherKrChar["더쇼"]="The Show"
#locations#
OtherKrChar["김포공항"]="金浦机场"
OtherKrChar["인천국제공항"]="仁川机场"
OtherKrChar["상주"]="尚州市"
OtherKrChar["울산"]="蔚山"
OtherKrChar["부산"]="釜山"
OtherKrChar["보라매"]="boramae"
OtherKrChar["영등포"]="永登浦"
OtherKrChar["타임스퀘어"]="时代广场"
OtherKrChar["대구"]="大邱"
OtherKrChar["인천공항"]="仁川机场"
OtherKrChar["강남"]="江南"
OtherKrChar["이화리"]="梨花女大"
# OtherKrChar[""]=""
OtherKrChar["일대백"]="1对100"
#event names e.g. to work/from work/入境/出境
OtherKrChar["출근길"]="上班"
OtherKrChar["퇴근길"]="下班"
OtherKrChar["퇴근"]="下班"
OtherKrChar["페스티벌"]="庆典"
OtherKrChar["팬싸인회"]="Fan sign"
OtherKrChar["팬사인회"]="Fan sign"
OtherKrChar["축하공연"]="庆祝演出"
OtherKrChar["출근"]="上班"
OtherKrChar["콘서트"]="演唱会"
OtherKrChar["핑크아일랜드"]="Pink Island"
OtherKrChar["출국"]="出境"
OtherKrChar["출퇴근"]="上下班"
OtherKrChar["입국"]="入境"
OtherKrChar["특집"]="特辑"
OtherKrChar["공연"]="公演"
# OtherKrChar[""]=""
OtherKrChar["녹화"]="预录"
OtherKrChar["리허설"]="彩排"
OtherKrChar["팬미팅"]="Fan Meeting"
OtherKrChar["서든어택"]="Sudden Attack"



ToBupdated =open("ToBupdated.txt","r")
ToBupdated_CN =open("ToBupdated_CN.txt","w")		
for line in ToBupdated:
	for KRs in GroupNames:
		num = re.sub(KRs, GroupNames[KRs], line)	
		line=num
	for KRs in OtherKrChar:
		num = re.sub(KRs, OtherKrChar[KRs], line)	
		line=num
	ToBupdated_CN.write(num)
ToBupdated.close()
ToBupdated_CN.close()
	
