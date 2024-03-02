// executed when date of birth is changed with onchange event  
function validateDateOfBirth(dateOfBirth){
    console.log('in validateDateOfBirth')
    console.log('dateOfBirth:',dateOfBirth)
    var regex = /^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$/;
    if (!regex.test(dateOfBirth)) {
        return $.Deferred().reject('Date must be in DD-MM-YYYY format');
    }

    var parts = dateOfBirth.split("-");
    var inputDate = new Date(parts[2], parts[1] - 1, parts[0]);
    console.log('inputDate: ',inputDate)
    var today = new Date();
    today.setHours(0,0,0,0);
    if (inputDate > today) {
        // console.log('inputDate:',inputDate)
        // console.log('today:',today)
        console.log('date is greater than current date')
        if(document.getElementById('parsley-id-3') !== null){
            document.getElementById('parsley-id-3').style.display='block'
        }
        document.getElementById('datepicker-date').classList.remove('parsley-success')
        document.getElementById('datepicker-date').classList.add('parsley-error')
        if (document.getElementById('parsley-id-3') != null){
            document.getElementById('parsley-id-3').childNodes[0].innerText = 'Date Of Birth Should be less than Current Date' 
        }
               
    } else if (isNaN(inputDate.getTime())) {
        console.log('invalid date')
        if(document.getElementById('parsley-id-3') !== null){
            document.getElementById('parsley-id-3').style.display='block'
        }
        document.getElementById('datepicker-date').classList.remove('parsley-success')
        document.getElementById('datepicker-date').classList.add('parsley-error')
    }else{
        if(document.getElementById('parsley-id-3') !== null){
            document.getElementById('parsley-id-3').style.display='none'
        }
        document.getElementById('datepicker-date').classList.add('parsley-success')
        document.getElementById('datepicker-date').classList.remove('parsley-error') 
    }
    
}

// data-parsley-valid-date-dd-mm-yyyy
// executed when next button is clicked 
Parsley.addValidator('validDateDdMmYyyy', {
    validateString: function(value) {
        console.log('in validateString for dob', value)
        var regex = /^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$/;
        if (!regex.test(value)) {
            return $.Deferred().reject('Date must be in DD-MM-YYYY format');
        }
    
        var parts = value.split("-");
        var inputDate = new Date(parts[2], parts[1] - 1, parts[0]);
        var today = new Date();
        today.setHours(0,0,0,0);
    
        if (inputDate > today) {
            document.getElementById('datepicker-date').classList.remove('parsley-success')
            document.getElementById('datepicker-date').classList.add('parsley-error')
            return $.Deferred().reject('Date Of Birth Should be less than Current Date');
        } else if (isNaN(inputDate.getTime())) {
            return $.Deferred().reject('Invalid date');
        }
        return true;
    },
    messages: {
      en: 'The date is not valid or is in the future.'
    }
  });
  
//   data-parsley-valid-gender
Parsley.addValidator('validGender', {
    validateString: function(value) {
        console.log('value in validGender:', value)
        // Check if the gender is either "Male" or "Female"
        if (value === 'Male' || value === 'Female') {
            console.log('in else at line 37')
            return true
        }else{
            console.log('in else at line 39')
            return $.Deferred().reject('This Value is Required');
        }
    },
    messages: {
        en: 'Please select either Male or Female.'
    }
});
  
Parsley.addValidator('validMobileNumber',{
    validateString: function(mobileNumber) {
        console.log('mobile number:', mobileNumber)
        console.log('mobile number type:', typeof mobileNumber)
        console.log("mobileNumber == +1: ", mobileNumber == +1)
        const pattern = /^\+\d+\s\d+$/;

    
        if (!mobileNumber) {
            console.log('The mobile number cannot be empty');
            return $.Deferred().reject('This Value is Required');
        }else if(mobileNumber.split(" ").length != 2){
            console.log('in else at line 39')
            return $.Deferred().reject('Please Select Country');
        }else if (!pattern.test(mobileNumber)) {
            console.log('The mobile number is not Valid');
            return $.Deferred().reject('The mobile number is not Valid')
        }else if (mobileNumber === ''){
            console.log('The mobile number cannot be empty');
            return $.Deferred().reject('This Value is Required');
        }else if (mobileNumber == +1){
            console.log('The mobile number cannot be empty');
            return $.Deferred().reject('This Value is Required');
        }else if(mobileNumber.split(" ")[0].charAt(0) !== '+'){
            console.log('in else at line 39')
            return $.Deferred().reject('Mobile Number is not Valid');
        }else{
            return true
        }
    }
})


async function submitFormData(formData) {
    console.log('submitting form data');
    for (const [key, value] of formData.entries()) {
        console.log('formData', key, ':', value);
    }
    try {
        const response = await fetch("/save_dependent", { // Ensure you replace "/save_dependent" with your actual endpoint
            method: "POST",
            headers: {
                "X-CSRFToken": document.querySelector('input[name="csrfmiddlewaretoken"]').value, // Pass the CSRF token in the request headers
                // Do not set 'Content-Type' manually; let the browser handle it for multipart/form-data boundary
            },
            body: formData,
        });
        // if (response.ok) {
        //     let data = await response.text(); // Assuming the server response is plain text. Use response.json() for JSON.
        //     console.log('Server Response:', data);
        // } else {
        //     // Handle HTTP error responses (e.g., 400, 401, 403, 404, 500)
        //     console.error('Server responded with non-OK status:', response.status);
        // }
        } catch (error) {
        console.error('Error:', error);
    }
}



(function($) {
    "use strict";
    $('#wizard2').steps({
        headerTag: 'h3',
        bodyTag: 'section',
        autoFocus: true,
        titleTemplate: '<span class="number">#index#<\/span> <span class="title">#title#<\/span>',
        onStepChanging: function(event, currentIndex, newIndex) {
            console.log('current index before step 1', currentIndex)
            if (currentIndex < newIndex) {
                // Step 1 form validation
                if (currentIndex === 0) {
                    let dob = $('#datepicker-date').parsley();
                    let gender = $('#user_gender').parsley();
                    let foreignAddress = $('#foreign_address').parsley();
                    // console.log('dob:',dob)
                    // console.log('gender.validate() :',gender.validate())
                    // console.log('gender.validate() == true:',gender.validate() == true)
                    // console.log('foreignAddress.validate() :',foreignAddress.validate())
                    if (dob.validate() == true && gender.validate() == true && foreignAddress.validate() == true) {
                        return true;
                    }else{
                        return false;
                        // return true;
                    }
                }
                console.log('current index before step 2', currentIndex)
                // // Step 2 form validation
                // if (currentIndex === 1) {
                //     console.log('in currentIndex === 1')
                //     var fname = $('#firstname').parsley();
                //     var lname = $('#lastname').parsley();
                //     var email = $('#email').parsley();
                //     if (fname.isValid() && lname.isValid() && email.isValid() ) {
                //         // return true;
                //     } else {
                //         fname.validate();
                //         lname.validate();
                //         email.validate();
                //     }
                // }
                // Always allow step back to the previous step even if the current step is not valid.
            } else {
                return true;
            }
        },
        onFinished: function (event, currentIndex){
            // console.log('finished event')
            let dob = $('#datepicker-date').parsley();
            let gender = $('#user_gender').parsley();
            let foreignAddress = $('#foreign_address').parsley();

            let fname = $('#firstname').parsley();
            let lname = $('#lastname').parsley();
            let email = $('#email').parsley();
            let mobile_number = $('#mobile-number').parsley();
            let dependent_address = $('#dependent_address').parsley();
            let current_issue_treatment_expected = $('#current_issue_treatment_expected').parsley();
            let health_insurance_details = $('#health_insurance_details').parsley();
            console.log('dob ',dob.$element.val());
            console.log('gender ',gender.$element.val());
            console.log('foreignAddress ',foreignAddress.$element.val());
            if (fname.isValid() && lname.isValid() && email.isValid() && mobile_number.isValid() && dependent_address.isValid()) {
                console.log('form submitting')

                // Create variables for each form field value using the existing Parsley instances
                let date_of_birth = dob.$element.val();
                let gender = gender.$element.val();
                let foreign_address = foreignAddress.$element.val();
                let firstNameValue = fname.$element.val();
                let lastNameValue = lname.$element.val();
                let emailValue = email.$element.val();
                let phoneNumberValue = document.getElementById('mobile-number').value;
                let dependentAddressValue = dependent_address.$element.val();
                let currentIssueTreatmentExpectedValue = current_issue_treatment_expected.$element.val();
                let healthInsuranceDetailsValue = health_insurance_details.$element.val();
                const fileInput = document.getElementById('dependent_doc');

                // Initialize the FormData object
                const formData = new FormData();

                // Append each variable to the formData object
                formData.append("date_of_birth", date_of_birth);
                formData.append("gender", gender);
                formData.append("foreign_address", foreign_address);
                formData.append("date_of_birth", date_of_birth);
                formData.append("first_name", firstNameValue);
                formData.append("first_name", firstNameValue);
                formData.append("first_name", firstNameValue);
                formData.append("last_name", lastNameValue);
                formData.append("email", emailValue);
                formData.append("phone_number", phoneNumberValue);
                formData.append("dependent_address", dependentAddressValue);
                formData.append("current_issue_treatment_expected", currentIssueTreatmentExpectedValue);
                formData.append("health_insurance_details", healthInsuranceDetailsValue);
                // formData.append("dependent_docs", dependentDocsValue);
                if (fileInput.files[0])  { // Check if any file is selected
                    formData.append("dependent_docs", fileInput.files[0]);
                }

                submitFormData(formData)
                return true;
            } else {
                fname.validate();
                lname.validate();
                email.validate();
                mobile_number.validate();
                dependent_address.validate();
                // current_issue_treatment_expected.validate();
                // health_insurance_details.validate();
                // dependent_docs.validate();
                
            }
        }
    });

    //_________accordion-wizard
    var options = {
        mode: 'wizard',
        autoButtonsNextClass: 'btn btn-primary float-end',
        autoButtonsPrevClass: 'btn btn-light',
        stepNumberClass: 'badge rounded-pill bg-primary me-1',
        onSubmit: function() {
            alert('Form submitted!');
            return true;
        }
    }

})(jQuery);