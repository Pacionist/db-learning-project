let server_address = "127.0.0.1"
let server_port = "8000"

let button = document.getElementById("reload-button");
let user_list = document.getElementById("user-list__list");
button.addEventListener("click", reload);

function reload() {
    fetch(`http://${server_address}:${server_port}/users/`)
        .then(res => res.json())
        .then(data => {replace_users_from_data(data)})
        .catch(error => console.log(error));
}

function replace_users_from_data(data) {
    user_list.innerHTML = "";
    data.users.forEach(user => {
        user_list.innerHTML += `<li>ID: ${user.user_id} Email: ${user.user_email} Username: ${user.user_name}</li>`;
    })
}