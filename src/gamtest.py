#!/usr/bin/env python3
"""Test GAMLite
"""

import gam
#GAMCFG = '/Library/Application Support/GAM/gam.cfg'
GAMCFG = '/Users/Ross/.gam/gam.cfg'
TESTGROUP = 'testgroup1@rdschool.org'
TESTGROUPALIAS = 'testgroup1alias@rdschool.org'
TESTOU = 'Fribble'
TESTOUPARENT = '/Test'
TESTSCHEMA = 'TestSchema'
TESTUSER = 'testuser1@rdschool.org'
TESTUSERALIAS = 'testuser1alias@rdschool.org'

gam.SetGlobalVariables(GAMCFG)
print(gam.Version())
print('\nCustomersGet')
result, status = gam.CustomersGet(None)
print(status, result)
print('\nDomainsGet')
result, status = gam.DomainsGet(None, None)
print(status, result)
print('\nDomainsList')
result, status = gam.DomainsList(None)
print(status, result)
print('\nGroupsGet')
result, status = gam.GroupsGet(groupKey=TESTGROUP, fields='*')
print(status, result)
print('\nGroupsList')
result, status = gam.GroupsList(fields='email,directMembersCount')
print(status, result)
print('\nGroupsAliasesInsert')
result, status = gam.GroupsAliasesInsert(TESTGROUP, TESTGROUPALIAS)
print(status, result)
print('\nGroupsAliasesList')
result, status = gam.GroupsAliasesList(TESTGROUP, fields='*')
print(status, result)
print('\nGroupsAliasesDelete')
result, status = gam.GroupsAliasesDelete(TESTGROUP, TESTGROUPALIAS)
print(status, result)
print('\nMembersGet')
result, status = gam.MembersGet(TESTGROUP, TESTUSER, fields='*')
print(status, result)
print('\nMembersList')
result, status = gam.MembersList(TESTGROUP, fields='email,id,role,status,type,delivery_settings')
print(status, result)
print('\nOrgunitsInsert')
result, status = gam.OrgunitsInsert(None, body={'name': TESTOU, 'parentOrgUnitPath': TESTOUPARENT})
print(status, result)
print('\nOrgunitsGet')
result, status = gam.OrgunitsGet(None, TESTOUPARENT+'/'+TESTOU)
print(status, result)
print('\nOrgunitsUpdate')
result, status = gam.OrgunitsUpdate(None, TESTOUPARENT+'/'+TESTOU, body={'description': 'Fribble'})
print(status, result)
print('\nOrgunitsList')
result, status = gam.OrgunitsList(None)
print(status, result)
print('\nOrgunitsDelete')
result, status = gam.OrgunitsDelete(None, TESTOUPARENT+'/'+TESTOU)
print(status, result)
print('\nSchemasInsert')
result, status = gam.SchemasInsert(None, body={'schemaName': TESTSCHEMA, 'displayName': TESTSCHEMA+' Display',
                                               'fields': [{'fieldName': 'BoolField', 'displayName': 'BoolField Display', 'fieldType': 'BOOL'}]})
print(status, result)
print('\nSchemasGet')
result, status = gam.SchemasGet(None, TESTSCHEMA)
print(status, result)
print('\nSchemasUpdate')
result, status = gam.SchemasUpdate(None, TESTSCHEMA, body={'schemaName': TESTSCHEMA,
                                                           'fields': [{'fieldName': 'IntField', 'displayName': 'IntField Display', 'fieldType': 'INT64'}]})
print(status, result)
print('\nSchemasList')
result, status = gam.SchemasList(None,)
print(status, result)
print('\nSchemasDelete')
result, status = gam.SchemasDelete(None, TESTSCHEMA)
print(status, result)
print('\nUsersGet')
result, status = gam.UsersGet(TESTUSER, fields='*')
print(status, result)
print('\nUsersList')
result, status = gam.UsersList(query='orgUnitPath:/Test', fields='primaryEmail,includeInGlobalAddressList,suspended')
print(status, result)
print('\nUsersAliasesInsert')
result, status = gam.UsersAliasesInsert(TESTUSER, TESTUSERALIAS)
print(status, result)
print('\nUsersAliasesList')
result, status = gam.UsersAliasesList(TESTUSER, fields='*')
print(status, result)
print('\nUsersAliasesDelete')
result, status = gam.UsersAliasesDelete(TESTUSER, TESTUSERALIAS)
print(status, result)
