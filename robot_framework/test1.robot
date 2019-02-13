*** Settings ***
Documentation    Suite description
Library  SSHLibrary
Library    res_utils.py
#Resource  ../rpc_excercises/rpc_excercise.py
*** Test Cases ***
#Test1
#    [Tags]    DEBUG
#    [Documentation]
##    open connection     xxmkt1055   prompt=${prompt_without_go}
##    SSHLibrary.Login    root    performance
##    Write Command   ls
##    Login to Prosys and Go Oltp
#    Log  IGT


Test2
    open connection  xxmkt1055  timeout=60  prompt=${prompt_without_go}
    SSHLibrary.login    root    performance
    set client configuration  prompt=${prompt_after_prosys}
    Write Command  su - prosys
    set client configuration  prompt=${prompt}
    Write Command   go oltp
    Run RPC
    should contain  ${outstr}   success

*** Keywords ***
Write Command
    [Arguments]    ${command}    ${verify_execution}=False
    [Documentation]    Writes command to ssh connection and reads output until prompt.
    ...    ${out} list is returned with lines from output (without command line and prompt)
    ...    ${outstr} is ${out} but converted to string (lines are joined)
    Read    delay=0.2 seconds
    Log    Writing command ${command}
    Write    ${command}
    Log    Waiting for output
    ${x}    Read Until Prompt
    ${x}=    Escape Ansi    ${x}
    Log    Command output: ${x}
    Log    Parsing output
    Set Suite Variable    ${out}    ${x.splitlines()[:-1]}
    ${outstr}    Join List    ${out}

    Set Suite Variable    ${outstr}
    Run Keyword If    '${verify_execution}'=='True'    Log    Verifying execution
    Run Keyword If    '${verify_execution}'=='True'    Write    echo $?
    ${x}    Run Keyword If    '${verify_execution}'=='True'    Read Until Prompt
    Run Keyword If    '${verify_execution}'=='True'    Should Be Equal As Integers    ${x.splitlines()[-2]}    0    Command ${command} failed. Command line output was:\n ${outstr}\nCheck robot logs for more details.

Login to Prosys and Go Oltp
    Write   su - prosys
    SET CLIENT CONFIGURATION  prompt=${prompt}
    Write Command   go oltp

Run RPC
    [Arguments]     ${user}=${user}
     ...            ${product}=${product}
     ...            ${function}=${function}
     ...            ${action}=${action}
     ...            ${draw}=${draw}
     ...            ${set_number}=${set_number}
     ...            ${win_numbers}=${win_numbers}
     ...            ${win_plus}=${win_plus}
     ...            ${win_power}=${win_power}
     ...            ${win_super}=${win_super}
     ...            ${win_promo}=${win_promo}
     ...            ${greenball}=${greenball}
     ...            ${multiplier}=${multiplier}
    Write Command   $USEC/bin/rpc -t ${user} -p ${product} ${function} ${action} ${draw} ${set_number} "${win_numbers}" "${win_plus}" ${win_power} ${win_super} ${win_promo} ${greenball} ${multiplier}

*** Variables ***
${prompt_without_go}   [root@xxmkt1055 ~]#
${prompt_after_prosys}  [xxmkt1055.gtk.gtech.com::prosys]:/home/prosys
${prompt}   [xxmkt1055.gtk.gtech.com:/oltp:prosys]:/oltp
${out}  ''
${user}     1
${function}     enter_win_nbrs
${product}  8
${action}   1
${draw}     1
${set_number}   1
${win_numbers}  1234567|
${win_plus}     8|
${win_power}    ""
${win_super}    ""
${win_promo}    ""
${greenball}    0
${multiplier}   0
