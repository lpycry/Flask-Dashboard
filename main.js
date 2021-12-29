/* login form validata*/

function validateLForm(){
    let email= document.forms["loginForm"]["email"].value;
    let pwd= document.forms["loginForm"]["pwd"].value;
    if(email==""||pwd==""){
        alert("Can not be empty!");
        return false;
    }
}


/* register from validata*/
function validateRForm(){
 let firstname = document.forms["registerForm"]["firstname"].value;
 let lastname = document.forms["registerForm"]["lastname"].value;
 let email = document.forms["registerForm"]["email"].value;
 let pwd = document.forms["registerForm"]["pwd"].value;
 let confirmPwd = document.forms["registerForm"]["confirmPwd"].value;
 if (firstname==""||lastname==""||email==""||pwd==""||confirmPwd==""){
    alert("Can not be empty!");
    return false;
    }
 if (pwd !=confirmPwd){
    alert("Password not matched!");
    return false;
 }
}
/* complanit data validation*/
function validateComplaintForm(){
    let caseNo = document.forms["complaintForm"]["caseNo"].value;
    let dateReceived =document.forms["complaintForm"]["dateReceived"].value;
    let status=document.forms["complaintForm"]["status"].value;
    let description=document.forms["complaintForm"]["description"].value;
    let rootCause=document.forms["complaintForm"]["rootCause"].value;
    let actions=document.forms["complaintForm"]["actions"].value;
    if(caseNo==""||dateReceived==""||status==""||description==""||rootCause==""||actions==""){
        alert("Please complete the data before submit!")
        return false;
    }

}

