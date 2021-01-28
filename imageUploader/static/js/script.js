$(document).ready(function() {
    /* BEGIN TASK 1 */

    // When the submit button is clicked execute the function below
    $("#submission").click(function(){
        // getting the data and using ajax to send data
        var formdata = new FormData($("#form")[0]);
        $.ajax({
            type: "POST",
            url : "/submit_image",
            data: formdata,
            dataType: "json",
            success: function(){
                document.location.href = "http://127.0.0.1:5000/submit_image"
            }
        });
    });
    /* END TASK 1 */
})