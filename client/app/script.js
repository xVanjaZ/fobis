document.addEventListener("DOMContentLoaded", function () {
    $("#notifModal").modal({
        backdrop: "static",
        keyboard: false
    })
    $("#findTrainBtn").on("click", function () {
        SendTrainNumber();
        $("#notifModal").modal("show")
    })
    $("#activateGPSBtn").on("click", function () {
        SendCoordinates();
        $("#notifModal").modal("show")
    })
})

//TODO: replace by backend
function SearchByTrainNumber(TrainNumber) {
    var result = []
    if (TrainNumber.length > 1 && TrainNumber.length < 6) {
        result[0] = 200;
        result[1] = "Meldingen Trein: '" + TrainNumber.toString() + "'";
        random = Math.floor(Math.random() * 2);
        switch (random) {
            case 0:
                result[2] = false;
                result[3] = "Nothing to report";
                break;
            case 1:
                result[2] = true;
                result[3] = "Volgend station arriveert deze trein op spoor 8 IPV. 12 ";
                break;
            case 2:
                result[2] = true;
                result[3] = "Trein is gestrand, hulptrein is onderweg";
                break;
        }
    } else {
        result[0] = 404;
        result[1] = "Trein niet gevonden";
        result[2] = false;
        result[3] = "";
    }
    return result;
}

//TODO: replace by backend
function SearchByCoordinates(latitude, longitude) {
    var result = []
    if (latitude !== null && longitude !== null) {
        result[0] = 200;
        result[1] = "Meldingen Trein: '" + Math.floor(Math.random() * 9999).toString() + "'";
        random = Math.floor(Math.random() * 2);
        switch (random) {
            case 0:
                result[2] = false;
                result[3] = "Nothing to report";
                break;
            case 1:
                result[2] = true;
                result[3] = "Volgend station arriveert deze trein op spoor 8 IPV. 12 ";
                break;
            case 2:
                result[2] = true;
                result[3] = "Trein is gestrand, hulptrein is onderweg";
                break;
        }
    } else {
        result[0] = 404;
        result[1] = "Trein niet gevonden";
        result[2] = false;
        result[3] = "";
    }
    return result;
}

function SendTrainNumber() {
    var Treinnummer = document.getElementById("TrainNumber").value;
    var train = SearchByTrainNumber(Treinnummer);
    var NotificationTitle = document.getElementById("NotificationTitle");
    var NotificationText = document.getElementById("NotificationText");
    console.log(train)
    if (train[0] === 200) {
        NotificationTitle.innerText = train[1];
        NotificationText.innerText = train[3];
        return train[2]
    } else if (train[0] === 404) {
        alert(train[1])
    } else {
        alert("[ERROR]:500 Internal Server Error")
    }
}

function SendCoordinates() {
    confirm("Please allow us to use your location");
    var x = 123;
    var y = 321;
    var NotificationTitle = document.getElementById("NotificationTitle");
    var NotificationText = document.getElementById("NotificationText");
    var train = SearchByCoordinates(x, y);
    if (train[0] === 200) {
        NotificationTitle.innerText = train[1];
        NotificationText.innerText = train[3];
    } else if (train[0] === 404) {
        alert(train[1])
    } else {
        alert("[ERROR]:500 Internal Server Error")
    }
}