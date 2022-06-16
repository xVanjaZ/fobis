document.addEventListener("DOMContentLoaded", function() {
    $("#notifModal").modal({
        backdrop: "static",
        keyboard: false
    })
    $("#findTrainBtn").on("click", function() {
        $("#notifModal").modal("show")
    })
    $("#activateGPSBtn").on("click", function() {
        $("#notifModal").modal("show")
    })
})