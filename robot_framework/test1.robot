*** Settings ***
Documentation    Suite description
Library  SSHLibrary
Library    res_utils.py

*** Test Cases ***
Test1
    [Tags]    DEBUG
    [Documentation]
    open connection     xxmkt1055   prompt=${prompt_without_go}
    SSHLibrary.Login    root    performance
    Write Command   ls
    Login to Prosys and Go Oltp
    Log  ${outstr}


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

*** Variables ***
${prompt_without_go}   [root@xxmkt1055 ~]#
${prompt}   [xxmkt1055.gtk.gtech.com:/oltp:prosys]:/oltp
${out}  ''