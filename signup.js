const signupButton = document.getElementById("signupbutton");
const signupModal = document.getElementById("signupmodal");

signupButton.addEventListener("click", () => {
    signupModal.style.display = "block";
});

window.addEventListener("click", (event) => {
    if(event.target === signupModal){
        signupModal.style.display = "none";
    }
});