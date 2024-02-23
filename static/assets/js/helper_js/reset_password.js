const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

console.log('in reset_pwd.js')

function toggle_password() {
  let confirm_password_field = document.querySelector('#confirm_password');
  confirm_password_field.type = 'text';
}

console.log('window.location.host',window.location.host);
// adding on_submit event listener to the form
document.addEventListener("DOMContentLoaded", function () {
  console.log(' in submit event')
  const form = document.querySelector("#reset_password_form");

  form.addEventListener("submit", async function (event) {
    // preventing form from reloading when submitted
    event.preventDefault();
    // fetching user entered details ie., email,password,confirm password
    const password = document.getElementById("reset_password").value;
    const confirm_password = document.getElementById("confirm_reset_password").value;
    

    console.log('user details', password, confirm_password)

    let error_in_signin_data = false

    document.getElementById('password_required_msg').style.display = 'none'
    document.getElementById('confirm_password_required_msg').style.display = 'none'

    document.getElementById("reset_password").style.borderColor = '#e3e3e3';
    document.getElementById("confirm_reset_password").style.borderColor = '#e3e3e3';

    // check if password is empty or not
    if (password.length == 0) {
      document.getElementById('password_required_msg').style.display = 'block'
      document.getElementById("reset_password").style.borderColor = 'red';
      error_in_signin_data = true
    }
    // check if password is empty or not
    if (confirm_password.length == 0) {
        document.getElementById('confirm_password_required_msg').style.display = 'block'
        document.getElementById("confirm_reset_password").style.borderColor = 'red';
        error_in_signin_data = true
    }
    // check if password is empty or not
    if (password != confirm_password) {
        document.getElementById('password_match_msg').style.display = 'block'
        document.getElementById("reset_password").style.borderColor = 'red';
        document.getElementById('confirm_password_match_msg').style.display = 'block'
        document.getElementById("confirm_reset_password").style.borderColor = 'red';
        error_in_signin_data = true
    }


    // Hash the password using MD5
    const hashedPassword = calcMD5(password);
    const hashedConfirmPassword = calcMD5(confirm_password);

    // fetching CSRF token from form
    const csrfToken = form.querySelector("[name='csrfmiddlewaretoken']").value;

    const formData = new FormData();

    formData.append("new_password", hashedPassword);
    formData.append("new_confirm_password", hashedConfirmPassword);

    // console log formData object values to make sure they are same as user entered values
    for (const value of formData.values()) {
      console.log('formData', value);
    }

    if (!error_in_signin_data) {
      try {
        const response = await fetch("", {
          method: "POST",
          headers: {
            "X-CSRFToken": csrfToken,
          },
          body: formData,
        });
        if (response.ok) {
          let data = await response.text();
        //   console.log('Server Response:', data);
          if (data == 'Password Reset Successful'){
            console.log('Password Reset Successful')
            window.location.href='http://'+window.location.host+'/auth/signin/'+'Reset Password Successful, Please Sign In';
          }
          else if (data === 'Reset Password Token not Expired') {
            document.getElementById('error_msg').innerText = 'Reset Password Link Sent, Kindly Check Your Mail';
            document.getElementById('error_container').style.display='block';
          } else if (data == "Reset Password Link Expired, Try Again") {
            // ex: http://127.0.0.1:8000/auth/reset_password/eyJhbGciOiJIUzI1N
            // window.location.host = 127.0.0.1:8000
            // forgot password page url: http://127.0.0.1:8000/auth/forgot_password_page
            // redirecting to for password page with error message as url parameter
            window.location.href='http://'+window.location.host+'/auth/forgot_password_page/'+'Reset Password Link Expired, Try Again';
          } else if (data == "Incorrect Email or Password. Please try again") {
            document.getElementById('error_msg').innerText = data;
            document.getElementById('error_container').style.display = 'block';
          }
          else {
            // Login failed, display error message
            document.getElementById('error_msg').innerText = 'Something went wrong, try again';
            document.getElementById('error_container').style.display = 'block';
          }
        }
      } catch (error) {
        console.error("Error:", error);
        // Handle the error
      }
    }

  });
});
