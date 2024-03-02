const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

//  script for phone number input field
//  source: 
//         https://github.com/Kenkarate/phone-number-validation/tree/master/build 
//         https://www.youtube.com/watch?v=aOCKMVE8zvQ&ab_channel=CodeWithAjesh

var input = document.querySelector('#phone');
console.log('input', input);
window.intlTelInput(input, {})

console.log('window.location.host',window.location.host);

function toggle_password() {
  let confirm_password_field = document.querySelector('#confirm_password');
  confirm_password_field.type = 'text';
}

// adding on_submit event listener to the form
document.addEventListener("DOMContentLoaded", function () {
  console.log(' in submit event')
  const form = document.querySelector("#signin-form");

  form.addEventListener("submit", async function (event) {
    // preventing form from reloading when submitted
    event.preventDefault();
    // fetching user entered details ie., email,password,confirm password
    const email = document.getElementById("signin_email").value;
    const password = document.getElementById("signin_password").value;
    const phonenumber = document.getElementById("phone").value;

    console.log('user details', email, password, phonenumber)

    let error_in_signin_data = false

    document.getElementById('email_required_msg').style.display = 'none'
    document.getElementById('valid_email_required_msg').style.display = 'none'
    document.getElementById('password_required_msg').style.display = 'none'
    document.getElementById('mobile_number_required_msg').style.display = 'none'

    document.getElementById("signin_email").style.borderColor = '#e3e3e3';
    document.getElementById("signin_password").style.borderColor = '#e3e3e3';
    document.getElementById("phone").style.borderColor = '#e3e3e3';



    let error_fields = []
    let error_message_array = []
    // check if email is empty or not
    if (email.length == 0) {
      // error_fields.push("signin_email")
      // error_message_array.push("Email")
      document.getElementById('email_required_msg').style.display = 'block'
      document.getElementById("signin_email").style.borderColor = 'red';
      error_in_signin_data = true
      console.log('error_in_signin_data',error_in_signin_data)
    }
    else {
      // Check if the email is in correct format
      if (!email.match(emailRegex)) {
        // error_fields.push("signin_email")
        // error_message_array.push("Valid Email")
        document.getElementById('valid_email_required_msg').style.display = 'block'
        document.getElementById("signin_email").style.borderColor = 'red';
        error_in_signin_data = true
        console.log('error_in_signin_data',error_in_signin_data)
      }
    }
    // check if password is empty or not
    if (password.length == 0) {
      // error_fields.push("signin_password")
      // error_message_array.push("Password")
      document.getElementById('password_required_msg').style.display = 'block'
      document.getElementById("signin_password").style.borderColor = 'red';
      error_in_signin_data = true
      console.log('error_in_signin_data',error_in_signin_data)
    }

    // console.log('error msg', error_message_array)
    // console.log('please enter',error_message_array)

    // // checks if any form field is causing an error or not
    // if(error_fields.length!==0){
    //   display_error_msg(error_message_array, error_fields, "")
    //   return;
    // }


    // Hash the password using MD5
    const hashedPassword = calcMD5(password);

    // fetching CSRF token from form
    const csrfToken = form.querySelector("[name='csrfmiddlewaretoken']").value;

    const formData = new FormData();

    formData.append("email", email);
    formData.append("hashedPassword", hashedPassword);

    // console log formData object values to make sure they are same as user entered values
    for (const value of formData.values()) {
      console.log('formData', value);
    }
    console.log('error_in_signin_data',error_in_signin_data)
    if (!error_in_signin_data) {
      try {
        const response = await fetch("/auth/signin", {
          method: "POST",
          headers: {
            "X-CSRFToken": csrfToken,
          },
          body: formData,
        });
        if (response.ok) {
          let data = await response.text();
          console.log('Server Response:', data);

          if (data === 'login_success') {
            // Successful login, redirect to index page
            console.log('Redirecting user');
            window.location.href = "/index";
          } else if (data == "No account found for this email. Please verify email or sign up") {
            // document.getElementById('')
            // console.log('No account found for this email. Please verify email or sign up')
            document.getElementById('error_msg').innerText = 'Incorrect Email or Password. Please try again';
            document.getElementById('error_container').style.display = 'block';
            display_error_msg([], [], data)
          } else if (data == "Incorrect Email or Password. Please try again") {
            // console.log('Incorrect Email or Password')
            // display_error_msg([],[],data)
            document.getElementById('error_msg').innerText = data;
            document.getElementById('error_container').style.display = 'block';
          }
          else {
            // Login failed, display error message
            display_error_msg([], [], 'Something went wrong, try again')
            document.getElementById('error_msg').innerText = 'Something went wrong, try again';
            document.getElementById('error_container').style.display = 'block';
          }
        }
      } catch (error) {
        console.error("Error:", error);
        // Handle the error
        display_error_msg("Something went wrong, try again", [])
      }
    }

  });
});

// function submit_func() {
//   console.log('in submit_func()')
//   var input = document.querySelector('#phone');
//   console.log('input', input);
//   window.intlTelInput(input, {})
// }