const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

// function hide_signup_msg() {
//   document.getElementById('signup_msg_div').style.display = 'none';
// }

// adding on_submit event listener to the form
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("#signup-form");
  console.log('form', form)
  form.addEventListener("submit", async function (event) {
    // preventing form from reloading when submitted
    event.preventDefault();
    
    const mobile_country_data = window.intlTelInputGlobals.getInstance(input).selectedCountryData;
    const fullName = document.getElementById("signup_fullname").value;
    const email = document.getElementById("signup_email").value;
    const dial_code = mobile_country_data.dialCode;
    const country = mobile_country_data.name;
    const phone_number = document.getElementById("phone").value;
    const password = document.getElementById("signup_password").value;
    const confirm_password = document.getElementById("signup_confirm_password").value;

    console.log('mobile_country_data:',mobile_country_data)
    console.log(' dial_code: ',dial_code,' country:', country)
  
    let error_in_signup_data = false

    document.getElementById('fullname_required_msg').style.display='none'
    document.getElementById('email_required_msg').style.display='none'
    document.getElementById('valid_email_required_msg').style.display='none'
    document.getElementById('phone_required_msg').style.display='none'
    document.getElementById('valid_phone_required_msg').style.display='none'
    document.getElementById('password_required_msg').style.display='none'
    document.getElementById('confirm_password_required_msg').style.display='none'
    document.getElementById('password_match_msg').style.display='none'
    document.getElementById('confirm_password_match_msg').style.display='none'

    document.getElementById("signup_fullname").style.borderColor = '#e3e3e3';
    document.getElementById("signup_email").style.borderColor = '#e3e3e3';
    document.getElementById("phone").style.borderColor = '#e3e3e3';
    document.getElementById("signup_password").style.borderColor = '#e3e3e3';
    document.getElementById("signup_confirm_password").style.borderColor = '#e3e3e3';

    

    // check if full name is empty or not
    if (fullName.length == 0) {
        document.getElementById('fullname_required_msg').style.display='block'
        document.getElementById("signup_fullname").style.borderColor = 'red';
        error_in_signup_data = true
      }
    // check if email is empty or not
    if (email.length == 0) {
        document.getElementById('email_required_msg').style.display='block'
        document.getElementById("signup_email").style.borderColor = 'red';
        error_in_signup_data = true
    } 
    else{
      // Check if the email is in correct format
      if (!email.match(emailRegex)) {
          document.getElementById('valid_email_required_msg').style.display='block'
          document.getElementById("signup_email").style.borderColor = 'red';
          error_in_signup_data = true
        }
    }
    // check if phone number is empty or not
    if (phone_number.length == 0) {
      document.getElementById('phone_required_msg').style.display='block'
      document.getElementById("phone").style.borderColor = 'red';
      error_in_signup_data = true
      }
    
    // check if password is empty or not
    if (password.length == 0) {
      document.getElementById('password_required_msg').style.display='block'
      document.getElementById("signup_password").style.borderColor = 'red';
      error_in_signup_data = true
    }
    // check if confirm password is empty or not
    if (confirm_password.length == 0) {
        document.getElementById('confirm_password_required_msg').style.display='block'
        document.getElementById("signup_confirm_password").style.borderColor = 'red';
        error_in_signup_data = true
      }


    // Hash the password using MD5
    const hashedPassword = calcMD5(password);
    const hashedConfirmPassword = calcMD5(confirm_password);
    console.log('user details', fullName, email, hashedPassword, phone_number, hashedConfirmPassword)

    if(hashedPassword != hashedConfirmPassword){
      document.getElementById('password_match_msg').style.display='block'
      document.getElementById("signup_password").style.borderColor = 'red';
      document.getElementById('confirm_password_match_msg').style.display='block'
      document.getElementById("signup_confirm_password").style.borderColor = 'red';
      error_in_signup_data = true
    }

    // fetching CSRF token from form 
    const csrfToken = form.querySelector("[name='csrfmiddlewaretoken']").value;

    const formData = new FormData();
    formData.append("full_name", fullName);
    formData.append("email", email);
    formData.append("hashedPassword", hashedPassword);
    formData.append("phone_number", phone_number);
    formData.append("dial_code", dial_code);
    formData.append("country", country);
    formData.append("hashedConfirmPassword", hashedConfirmPassword);

    // console log formData object values to make sure they are same as user entered values 
    for (const value of formData.values()) {
      console.log('formData', value);
    }


    if(!error_in_signup_data){
      console.log('error_in_signup_data', error_in_signup_data)
      // sending data to backend
      try {
        // displaying loader
      document.getElementById('global-loader').style.display='block';
      
        const response = await fetch("", {
          method: "POST",
          headers: {
            "X-CSRFToken": csrfToken,
          },
          body: formData,
        });
        if (response.ok) {
          let data = await response.text();
          // console.log('Server Response:', data);

          if (data === 'signup_success') {
            // displaying loader
            document.getElementById('global-loader').style.display='none';
            // Successful login, redirect to index page
            let signup_msg_div = document.getElementById('signup_msg_div');
            signup_msg_div.classList.add("alert-success");
            let msg = document.getElementById('signup_msg');
            msg.innerText='User Registered Succesfully';
            signup_msg_div.style.display = 'block';

            // let signup_msg_div = document.getElementById('signup_msg_div');
            // signup_msg_div.classList.add("alert-danger");
            // let msg = document.getElementById('signup_msg');
            // msg.innerText='This email is already registered. Please use a different email';
            // signup_msg_div.style.display = 'block';
            console.log('redirect user');
            window.location.href = "/auth/signin";
            return;
          } else if (data = "This email is already registered. Please use a different email"){
              console.log('in different email');
              // displaying loader
              document.getElementById('global-loader').style.display='none';

              // displaying signup message
              let signup_msg_div = document.getElementById('signup_msg_div');
              signup_msg_div.classList.add("alert-danger");
              let msg = document.getElementById('signup_msg');
              msg.innerText='This email is already registered. Please use a different email';
              signup_msg_div.style.display = 'block';
          }
          else{
            // displaying loader
            document.getElementById('global-loader').style.display='none';

            // displaying signup message
            let signup_msg_div = document.getElementById('signup_msg_div');
            signup_msg_div.classList.add("alert-danger");
            let msg = document.getElementById('singup_msg');
            msg.innerText='Something went wrong, Try Again';
            signup_msg_div.style.display = 'block';
          }
          }
        } catch (error) {
        // displaying loader
        document.getElementById('global-loader').style.display='none';  

        // displaying signup message
        let signup_msg_div = document.getElementById('signup_msg_div');
        signup_msg_div.classList.add("alert-danger");
        let msg = document.getElementById('signup_msg');
        msg.innerText='Something went wrong, Try Again';
        signup_msg_div.style.display = 'block';
      }
    }
  });
});


function hide_signup_msg_div(){
  console.log("in hide_signup_msg_div")
  document.getElementById('signup_msg_div').style.display='none';
}


function preventSpace(event) {
  if (event.key === ' ') {
      // console.log("space entered")
      event.preventDefault();
  }
}

