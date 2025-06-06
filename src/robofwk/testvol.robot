*** Settings ***
Library           RequestsLibrary
Suite Setup       Create Session    volapi    http://localhost:5000

*** Variables ***
${BASE_URL}       http://localhost:5000
${VOL_ENDPOINT}   /vols/123

*** Test Cases ***
Charger Un Vol Par Son Numéro
    [Tags]    api    vol
    ${response}=    GET    volapi    ${VOL_ENDPOINT}
    Status Should Be    200    ${response}
    Dictionary Should Contain Key    ${response.json()}    numero
    Dictionary Should Contain Value  ${response.json()}    123
    Dictionary Should Contain Key    ${response.json()}    destination
    Dictionary Should Contain Key    ${response.json()}    avion_id

*** Keywords ***
Status Should Be
    [Arguments]    ${expected_status}    ${response}
    Should Be Equal As Numbers    ${response.status_code}    ${expected_status}
