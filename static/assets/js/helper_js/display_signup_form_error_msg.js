// function to display form validation errors and error messages
function display_error_msg(error_msg_array, error_fields, error_message_string, field_required_msg_array) {
    console.log('in display_error_msg');
  
    let final_error_message = "";


    // if(error_msg_array.length == 3){
    //   final_error_message += `Please enter ${error_msg_array[0]}, ${error_msg_array[1]} and ${error_msg_array[2]}`
    // }
    // if(error_msg_array.length == 2){
    //   final_error_message += `Please enter ${error_msg_array[0]} and ${error_msg_array[1]}`
    // }
    // if(error_msg_array.length == 1){
    //   if(error_msg_array.includes("Password and Confirm Password do not match")){
    //     console.log("Password and Confirm Password do not match")
    //     final_error_message = `Password and Confirm Password do not match`
    //   }else{
    //     final_error_message += `Please enter ${error_msg_array[0]}`
    //   }
    // }

    if(error_message_string){
      console.log('error_message_string',error_message_string)
      final_error_message += error_message_string
    }

    if(error_msg_array.includes("Password and Confirm Password do not match")){
      console.log("Password and Confirm Password do not match")
      final_error_message = `Password and Confirm Password do not match`
    }

    
  
    // Create a new element to display the error message
    const errorElement = document.createElement("div");
    errorElement.classList.add("alert", "alert-outline-danger", "mg-b-0", "alert-dismissible", "fade", "show");
    errorElement.setAttribute("role", "alert");
    errorElement.textContent = final_error_message;
  
    // Create the close button element
    const closeButton = document.createElement("button");
    closeButton.classList.add("btn-close");
    closeButton.setAttribute("aria-label", "Close");
    closeButton.setAttribute("data-bs-dismiss", "alert");
    closeButton.setAttribute("type", "button");
  
    // Create the <span> element for the "x" icon
    const closeIconSpan = document.createElement("span");
    closeIconSpan.setAttribute("aria-hidden", "true");
    closeIconSpan.innerHTML = "&times;";
  
    // Append the <span> to the close button
    closeButton.appendChild(closeIconSpan);
  
    // Append the close button to the error element
    errorElement.appendChild(closeButton);
  
    // // Find the location where you want to display the error message
    // const errorContainer = document.getElementById("error-container"); // Replace with the actual ID
  
    // // Append the error element to the container
    // errorContainer.appendChild(errorElement);
  
    // adding red border to form fields to indicate empty or invalid input 
    for (let error_div = 0; error_div < error_fields.length; error_div++) {
      console.log(error_fields[error_div])
      document.getElementById(error_fields[error_div]).style.borderColor = "red";
    }
    return;
  }
  
  
    