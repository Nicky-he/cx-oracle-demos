#!/usr/anim/bin/pypix

attributes=[
'ACTION',
'AUDITED_CURSORID',
'AUTHENTICATED_IDENTITY',
'AUTHENTICATION_DATA',
'AUTHENTICATION_METHOD',
'BG_JOB_ID',
'CLIENT_IDENTIFIER',
'CLIENT_INFO',
'CURRENT_BIND',
'CURRENT_SCHEMA',
'CURRENT_SCHEMAID',
'CURRENT_SQL',
'CURRENT_SQLn',
'CURRENT_SQL_LENGTH',
'DB_DOMAIN',
'DB_NAME',
'DB_UNIQUE_NAME',
'ENTRYID',
'ENTERPRISE_IDENTITY',
'FG_JOB_ID',
'GLOBAL_CONTEXT_MEMORY',
'GLOBAL_UID',
'HOST',
'IDENTIFICATION_TYPE',
'INSTANCE',
'INSTANCE_NAME',
'IP_ADDRESS',
'ISDBA',
'LANG',
'LANGUAGE',
'MODULE',
'NETWORK_PROTOCOL',
'NLS_CALENDAR',
'NLS_CURRENCY',
'NLS_DATE_FORMAT',
'NLS_DATE_LANGUAGE',
'NLS_SORT',
'NLS_TERRITORY',
'OS_USER',
'POLICY_INVOKER',
'PROXY_ENTERPRISE_IDENTITY',
#'PROXY_GLOBAL_UID',
'PROXY_USER',
'PROXY_USERID',
'SERVER_HOST',
'SERVICE_NAME',
'SESSION_USER',
'SESSION_USERID',
'SESSIONID',
'SID',
'STATEMENTID',
'TERMINAL'
]

import cx_Oracle
connstr = "templar/oracle@templar"
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

print dir(curs)
for a in attributes:
    curs.execute("select sys_context('USERENV', '%s') from dual"%(a))
    print a,curs.fetchall()
