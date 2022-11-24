const form = document.getElementById('formnovo')
const pega = document.getElementById('pegou')
var criou = 0;

form.onsubmit = function (e) {

	e.preventDefault();
	const inputField = document.getElementById('taskinput');
	addTask(inputField.value);
	form.reset();
};

function addTask(description) {

	if (criou < 5) {


	const taskContainer = document.createElement('div');
	const taskSubmit = document.createElement('div')
	const newTask = document.createElement('input');


	const taskDescriptionNode = document.createTextNode(description);
	newTask.setAttribute('type', 'text');
	newTask.setAttribute('name', criou);
	newTask.setAttribute('id', description);
	criou = criou + 1;

    criarElemento = document.createElement('input');

	taskContainer.classList.add('task-item');
	taskContainer.appendChild(newTask);
	taskContainer.appendChild(taskLabel);

    taskSubmit.classList.add('task-submit');
	taskSubmit.appendChild(criarElemento);

	taskList.appendChild(taskContainer);
	taskList.appendChild(taskSubmit);

	};
};

