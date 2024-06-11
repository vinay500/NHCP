// executed when date of birth is changed with onchange event  
function validateDateOfBirth(dateOfBirth){
    // console.log('in validateDateOfBirth')
    // console.log('dateOfBirth:',dateOfBirth)
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
        // console.log('date is greater than current date')
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

function validateDependentDateOfBirth(dateOfBirth){
    // console.log('in validateDateOfBirth')
    // console.log('dateOfBirth:',dateOfBirth)
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
        // console.log('date is greater than current date')
        if(document.getElementById('parsley-id-17') !== null){
            document.getElementById('parsley-id-17').style.display='block'
        }
        document.getElementById('dependent_datepicker-date').classList.remove('parsley-success')
        document.getElementById('dependent_datepicker-date').classList.add('parsley-error')
        if (document.getElementById('parsley-id-17') != null){
            document.getElementById('parsley-id-17').childNodes[0].innerText = 'Date Of Birth Should be less than Current Date' 
        }
               
    } else if (isNaN(inputDate.getTime())) {
        console.log('invalid date')
        if(document.getElementById('parsley-id-17') !== null){
            document.getElementById('parsley-id-17').style.display='block'
        }
        document.getElementById('dependent_datepicker-date').classList.remove('parsley-success')
        document.getElementById('dependent_datepicker-date').classList.add('parsley-error')
    }else{
        if(document.getElementById('parsley-id-17') !== null){
            document.getElementById('parsley-id-17').style.display='none'
        }
        document.getElementById('dependent_datepicker-date').classList.add('parsley-success')
        document.getElementById('dependent_datepicker-date').classList.remove('parsley-error') 
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
        // console.log('value in validGender:', value)
        // Check if the gender is either "Male" or "Female"
        if (value === 'Male' || value === 'Female') {
            // console.log('in else at line 37')
            return true
        }else{
            // console.log('in else at line 39')
            return $.Deferred().reject('This Value is Required');
        }
    },
    messages: {
        en: 'Please select either Male or Female.'
    }
});


//data-parsley-valid-gender
Parsley.addValidator('validRelation', {
    validateString: function(value) {
        // console.log('value in validGender:', value)
        // Check if the gender is either "Male" or "Female"
        if (value === 'Father' || value === 'Mother' || value === 'Husband' || value === 'Wife' || value === 'Son' || value === 'Daughter'
            || value === 'Sibling' || value === 'Grand Father' || value === 'Grand Mother' || value === 'Father In Law' || value === 'Mother In Law') {
            // console.log('in else at line 37')
            return true
        }else{
            // console.log('in else at line 39')
            return $.Deferred().reject('This Value is Required');
        }
    },
    messages: {
        en: 'Please select either Male or Female.'
    }
});
  
// validDateDdMmYyyy
// data-parsley-valid-date-dd-mm-yyyy
// validDateDependentDdMmYyyy
// data-parsley-valid-date-dependent-dd-mm-yyyy
// executed when next button is clicked 
Parsley.addValidator('validDateDependentDdMmYyyy', {
    validateString: function(value) {
        console.log('in validDateDependentDdMmYyyy', value)
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


Parsley.addValidator('validMobileNumber',{
    validateString: function(mobileNumber) {
        // console.log('mobile number:', mobileNumber)
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
    console.log('submitting form data in submitFormData');

    for (const [key, value] of formData.entries()) {
        console.log('formData', key, ':', value);
    }
    try{
        console.log('submitting using this.submit()')
        document.getElementById('global-loader').style.display="block";
        document.getElementById("add_dependent_form").submit();
    }catch (error) {
            console.error('Error:', error);
    }
}


function dynamic_add_dependent_section(){
    
    let no_of_add_dependent_section = $('section').filter(function () {
        // Check if the current section contains an input with name='first_name'
        return $(this).find('input[name="firstname"]').length > 0;
    }).filter(function () {
        // Further filter those sections whose ID matches the pattern
        return this.id.match(/wizard2-p-\d+/);
    });
    console.log('no_of_add_dependent_section: ',no_of_add_dependent_section.length);

    const sectionIndex = no_of_add_dependent_section.length + 1;

    $('#wizard2').steps('add', 
    {title: 'Add Dependent', content: `
            <div class="row">
            <div class="col-md-6">
                <label class="form-label">Firstname <span class="tx-danger">*</span></label> <input class="form-control" id="firstname_${sectionIndex}" name="firstname" placeholder="Enter firstname"  type="text" required>
            </div>
            <div class="col-md-6 mg-t-20 mg-md-t-0">
                <label class="form-label">Lastname <span class="tx-danger">*</span></label> <input class="form-control" id="lastname_${sectionIndex}" name="lastname" placeholder="Enter lastname"  type="text" required>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6">
                <label class="form-label">Email <span class="tx-danger">*</span></label>
                <input class="form-control" id="email_${sectionIndex}" name="email" placeholder="Enter email address"  type="email" required>
            </div>
            <div class="col-md-6">
                <label class="form-label">Phone Number <span class="tx-danger">*</span></label>
                <div class="input-group telephone-input ">
                    <input  class="form-control" type="tel" id="mobile-number_${sectionIndex}" placeholder="e.g. +1 702 123 4567" required data-parsley-valid-mobile-number>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6">
                <label for="dependent_address" class="form-label">Address  <span class="tx-danger">*</span></label>
                <textarea id="dependent_address_${sectionIndex}" class="form-control" placeholder="Enter Address" rows="3" required ></textarea>
            </div>
            <div class="col-md-6">
                <label for="current_issue_treatment_expected" class="form-label">Current Issue and Treatment Expected</label>
                <textarea id="current_issue_treatment_expected_${sectionIndex}" class="form-control" placeholder="" rows="3"  ></textarea>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6">
                <label for="health_insurance_details" class="form-label">Health Insurance Details</label>
                <textarea id="health_insurance_details_${sectionIndex}" class="form-control" placeholder="" rows="3"  ></textarea>
            </div>
            <div class="col-md-6">
                <label for="dependent_docs" class="form-label">Any Documents</label>
                <input type="file" id="dependent_doc_${sectionIndex}" class="dropify" data-height="85" />
            </div>
        </div>
    `
    })
}


(function($) {
    "use strict";
    let add_dependent_wizard = $('#wizard2').steps({
        headerTag: 'h3',
        bodyTag: 'section',
        autoFocus: true,
        titleTemplate: '<span class="number">#index#<\/span> <span class="title">#title#<\/span>',
        onStepChanging: function(event, currentIndex, newIndex) {
            console.log('currentIndex:',currentIndex)
            console.log('newIndex:',newIndex)
            
            if (currentIndex < newIndex) {
                // Step 1 form validation
                if (currentIndex === 0) {
                    let dob = $('#datepicker-date').parsley();
                    let gender = $('#user_gender').parsley();
                    let foreignAddress = $('#foreign_address').parsley();
                    console.log('dob:',dob)
                    console.log('dob.validate() :',dob.validate())
                    // // console.log('gender.validate() == true:',gender.validate() == true)
                    // console.log('foreignAddress.validate() :',foreignAddress.validate())
                    if (dob.validate() == true && gender.validate() == true && foreignAddress.validate() == true) {
                        document.getElementById('addMoreDependents').style.display='block';
                        document.getElementById('add_dependent_cant_change_div').style.display='block';
                        return true;
                    }else{
                        dob.validate()
                        gender.validate()
                        foreignAddress.validate()
                        // return false;
                    }
                }
                // Step 2 form validation
                if (currentIndex === 1) {
                    console.log('in currentIndex === 1')
                    let fname = $('#firstname').parsley();
                    let lname = $('#lastname').parsley();
                    let email = $('#email').parsley();
                    let mobile_number = $('#mobile-number').parsley();
                    let dependent_address = $('#dependent_address').parsley();
                    let current_issue_treatment_expected = $('#current_issue_treatment_expected').parsley();
                    let health_insurance_details = $('#health_insurance_details').parsley();
        
                    if (fname.isValid() && lname.isValid() && email.isValid() && mobile_number.isValid() && dependent_address.isValid()) {
                        console.log('form submitting')

                        // Create variables for each form field value using the existing Parsley instances
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

                        // submitFormData(formData)
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
                // Step 3 form validation
                if (currentIndex === 2) {
                    console.log('in currentIndex === 2')
                    let fname = $('#firstname').parsley();
                    let lname = $('#lastname').parsley();
                    let email = $('#email').parsley();
                    let mobile_number = $('#mobile-number').parsley();
                    let dependent_address = $('#dependent_address').parsley();
                    let current_issue_treatment_expected = $('#current_issue_treatment_expected').parsley();
                    let health_insurance_details = $('#health_insurance_details').parsley();
        
                    if (fname.isValid() && lname.isValid() && email.isValid() && mobile_number.isValid() && dependent_address.isValid()) {
                        console.log('form submitting')

                        // Create variables for each form field value using the existing Parsley instances
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

                        // submitFormData(formData)
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
                // Always allow step back to the previous step even if the current step is not valid.
            } else {
                return true;
            }
        },
        onInit: function(event, currentIndex, newIndex){
            
            console.log('currentIndex:',currentIndex)
            console.log('newIndex:',newIndex)
            // Assuming the "Add Dependent" button needs to be dynamically added
            // Find the ul element created by jQuery Steps
            var $ul = $('ul[role="menu"]');
            
            // Create the "Add Dependent" li item
            if(document.getElementById('datepicker-date')){
                console.log("in document.getElementById('datepicker-date') - true")
                var $addDependentLi = $(`<li aria-hidden="false" aria-disabled="false"><a id="addMoreDependents" role="menuitem" onclick="save_dependent_and_add_another()" style="display:none;cursor:pointer;">Save and Add Another</a></li>`);
                document.getElementById('add_dependent_cant_change_div').style.display='none';
            }else{
                console.log("in document.getElementById('datepicker-date') - false")
                var $addDependentLi = $(`<li aria-hidden="false" aria-disabled="false"><a id="addMoreDependents" role="menuitem" onclick="save_dependent_and_add_another()">Save and Add Another</a></li>`);
                document.getElementById('add_dependent_cant_change_div').style.display='block';
            }
            
            
            // Insert the "Add Dependent" button before the "Next" button
            // Adjust the insertBefore selector as necessary based on your markup
            $addDependentLi.insertBefore($ul.find('li').eq(1)); 
            // Assuming "Next" is now the third item

            
        },
        onFinished: function (event, currentIndex){
            console.log('finished event')
            let dob,gender,foreignAddress = null;
            if ($('#datepicker-date').length) {
                dob = $('#datepicker-date').parsley();
            }
            
            if ($('#user_gender').length) {
                gender = $('#user_gender').parsley();
            }
            
            if ($('#foreign_address').length) {
                foreignAddress = $('#foreign_address').parsley();
            }
            
            let fname = $('#firstname').parsley();
            let lname = $('#lastname').parsley();
            let email = $('#email').parsley();
            let mobile_number = $('#mobile-number').parsley();
            let dependent_dob = $('#dependent_datepicker-date').parsley();
            let dependent_gender = $('#dependent_gender').parsley();
            let dependent_relation = $('#relation').parsley();
            let dependent_address = $('#dependent_address').parsley();
            let current_issue_treatment_expected = $('#current_issue_treatment_expected').parsley();
            let health_insurance_details = $('#health_insurance_details').parsley();
            if (dob && gender && foreignAddress) {
                console.log('dob:', dob.$element.val());
                console.log('gender:', gender.$element.val());
                console.log('foreignAddress:', foreignAddress.$element.val());
            }
            if (fname.isValid() && lname.isValid() && email.isValid() && mobile_number.isValid() && dependent_address.isValid() 
                && dependent_dob.isValid() && dependent_gender.isValid() && dependent_relation.isValid()) {
                console.log('form submitting')
                // Initialize the FormData object
                const formData = new FormData();
                if (dob) {
                    let date_of_birth = dob.$element.val();
                    formData.append("date_of_birth", date_of_birth);
                }
                if (gender) {
                    let genderValue = gender.$element.val();
                    formData.append("gender", genderValue);
                }
                if (foreignAddress) {
                    let foreign_address = foreignAddress.$element.val();
                    formData.append("foreign_address", foreign_address);
                }
                let firstNameValue = fname.$element.val();
                let lastNameValue = lname.$element.val();
                let emailValue = email.$element.val();
                let dobValue = dependent_dob.$element.val();
                let dependent_gender_value = dependent_gender.$element.val();
                let dependent_relation_value = dependent_relation.$element.val();
                let phoneNumberValue = document.getElementById('mobile-number').value;
                let dependentAddressValue = dependent_address.$element.val();
                let currentIssueTreatmentExpectedValue = current_issue_treatment_expected.$element.val();
                let healthInsuranceDetailsValue = health_insurance_details.$element.val();
                const fileInput = document.getElementById('dependent_doc');

                

                // Append each variable to the formData object
                // formData.append("date_of_birth", date_of_birth);
                // formData.append("gender", genderValue);
                // formData.append("foreign_address", foreign_address);
                formData.append("first_name", firstNameValue);
                formData.append("last_name", lastNameValue);
                formData.append("email", emailValue);
                formData.append("dependent_dob", dobValue);
                formData.append("dependent_gender", dependent_gender_value);
                formData.append("dependent_relation", dependent_relation_value);
                formData.append("phone_number", phoneNumberValue);
                formData.append("dependent_address", dependentAddressValue);
                formData.append("current_issue_treatment_expected", currentIssueTreatmentExpectedValue);
                formData.append("health_insurance_details", healthInsuranceDetailsValue);
                // formData.append("dependent_docs", dependentDocsValue);
                if (fileInput.files[0])  { // Check if any file is selected
                    formData.append("dependent_docs", fileInput.files[0]);
                }
                document.getElementById('finished').disabled = false;
                // document.getElementById('finished').hidden = false;
                document.getElementById('finished').checked=true;

                let selectedCountryElement = document.querySelector('.country-list .country.active');
                // Check if a country is selected
                if (selectedCountryElement) {
                    // console.log('in selectedCountryElement')
                    // Extract country information
                    var countryName = selectedCountryElement.querySelector('.country-name').textContent;
                    var dialCode = selectedCountryElement.querySelector('.dial-code').textContent;
                    var countryCode = selectedCountryElement.getAttribute('data-country-code');

                    // Print or use the extracted information as needed
                    console.log('Selected Country:', countryName);
                    console.log('Dial Code:', dialCode);
                    console.log('Country Code:', countryCode);

                    document.getElementById('country').disabled = false;
                    document.getElementById('country').value = countryName;
                    
                } 
                console.log("document.getElementById('country').value: ",document.getElementById('country').value);
                submitFormData(formData)
                return true;
            } else {
                fname.validate();
                lname.validate();
                email.validate();
                mobile_number.validate();
                dependent_address.validate();
                dependent_dob.validate();
                dependent_gender.validate();
                dependent_relation.validate();
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


function save_dependent_and_add_another(){
    console.log('in save_dependent_and_add_another')
            let dob = null
            let gender = null
            let foreignAddress = null
            if ($('#datepicker-date').length) {
                dob = $('#datepicker-date').parsley();
            }
            
            if ($('#user_gender').length) {
                gender = $('#user_gender').parsley();
            }
            
            if ($('#foreign_address').length) {
                foreignAddress = $('#foreign_address').parsley();
            }
            

            let fname = $('#firstname').parsley();
            let lname = $('#lastname').parsley();
            let email = $('#email').parsley();
            let mobile_number = $('#mobile-number').parsley();
            let dependent_dob = $('#dependent_datepicker-date').parsley();
            let dependent_gender = $('#dependent_gender').parsley();
            let dependent_relation = $('#relation').parsley();
            let dependent_address = $('#dependent_address').parsley();
            let current_issue_treatment_expected = $('#current_issue_treatment_expected').parsley();
            let health_insurance_details = $('#health_insurance_details').parsley();
            if (dob && gender && foreignAddress) {
                console.log('dob:', dob.$element.val());
                console.log('gender:', gender.$element.val());
                console.log('foreignAddress:', foreignAddress.$element.val());
            }
            if (fname.isValid() && lname.isValid() && email.isValid() && mobile_number.isValid() && dependent_address.isValid() 
                && dependent_dob.isValid() && dependent_gender.isValid() && dependent_relation.isValid()) {
                console.log('form submitting')
                // Initialize the FormData object
                const formData = new FormData();
                if (dob) {
                    let date_of_birth = dob.$element.val();
                    formData.append("date_of_birth", date_of_birth);
                }
                if (gender) {
                    let genderValue = gender.$element.val();
                    formData.append("gender", genderValue);
                }
                if (foreignAddress) {
                    let foreign_address = foreignAddress.$element.val();
                    formData.append("foreign_address", foreign_address);
                }
                let firstNameValue = fname.$element.val();
                let lastNameValue = lname.$element.val();
                let emailValue = email.$element.val();
                let dobValue = dependent_dob.$element.val();
                let dependent_gender_value = dependent_gender.$element.val();
                let dependent_relation_value = dependent_relation.$element.val();
                let phoneNumberValue = document.getElementById('mobile-number').value;
                let dependentAddressValue = dependent_address.$element.val();
                let currentIssueTreatmentExpectedValue = current_issue_treatment_expected.$element.val();
                let healthInsuranceDetailsValue = health_insurance_details.$element.val();
                const fileInput = document.getElementById('dependent_doc');

                

                // Append each variable to the formData object
                // formData.append("date_of_birth", date_of_birth);
                // formData.append("gender", genderValue);
                // formData.append("foreign_address", foreign_address);
                formData.append("first_name", firstNameValue);
                formData.append("last_name", lastNameValue);
                formData.append("email", emailValue);
                formData.append("dependent_dob", dobValue);
                formData.append("dependent_gender", dependent_gender_value);
                formData.append("dependent_relation", dependent_relation_value);
                formData.append("phone_number", phoneNumberValue);
                formData.append("dependent_address", dependentAddressValue);
                formData.append("current_issue_treatment_expected", currentIssueTreatmentExpectedValue);
                formData.append("health_insurance_details", healthInsuranceDetailsValue);
                // formData.append("dependent_docs", dependentDocsValue);
                if (fileInput.files[0])  { // Check if any file is selected
                    formData.append("dependent_docs", fileInput.files[0]);
                }
                let selectedCountryElement = document.querySelector('.country-list .country.active');
                // Check if a country is selected
                if (selectedCountryElement) {
                    // console.log('in selectedCountryElement')
                    // Extract country information
                    var countryName = selectedCountryElement.querySelector('.country-name').textContent;
                    var dialCode = selectedCountryElement.querySelector('.dial-code').textContent;
                    var countryCode = selectedCountryElement.getAttribute('data-country-code');

                    // Print or use the extracted information as needed
                    console.log('Selected Country:', countryName);
                    console.log('Dial Code:', dialCode);
                    console.log('Country Code:', countryCode);

                    document.getElementById('country').disabled = false;
                    document.getElementById('country').value = countryName;
                    
                } 
                console.log("document.getElementById('country').value: ",document.getElementById('country').value);
                submitFormData(formData)
                return true;
            } else {
                fname.validate();
                lname.validate();
                email.validate();
                mobile_number.validate();
                dependent_address.validate();
                dependent_dob.validate();
                dependent_gender.validate();
                dependent_relation.validate();
            }
}

function preventSpace(event) {
    if (event.key === ' ') {
        // console.log("space entered")
        event.preventDefault();
    }
}