
var currentNumberWrapper = document.getElementById('currentNumber')
var currentNumber = 0;


function increment() {

        currentNumber = currentNumber + 1;
        currentNumberWrapper.innerHTML = currentNumber;

}
function decrement() {

        currentNumber = currentNumber - 1;
        currentNumberWrapper.innerHTML = currentNumber;

}




const form = document.getElementById('task-form');
const taskList = document.getElementById('tasks');
const inputtype = document.getElementById('inputhidden');
var criou = 0;
var criado = 0;

form.onsubmit = function (e) {
     if (criou < 5) {
	e.preventDefault();
	const inputField = document.getElementById('task-input');
	addTask(inputField.value);
	form.reset();
	};
};

function addTask(description) {

    if (criou < 5) {
	const taskContainer = document.createElement('div');
	const taskSubmit = document.createElement('div')
	const newTask = document.createElement('input');
	const taskLabel = document.createElement('label');
	editType = document.getElementById('inputhidden');
	criarContagem = document.getElementById('inputcontagem');

	if (criado < 1) {
        criarElemento = document.createElement('input');
        criado = criado + 1;
	};



	const taskDescriptionNode = document.createTextNode(description);
	newTask.setAttribute('type', 'text');
	newTask.setAttribute('name', criou);
	newTask.setAttribute('id', description);
	editType.setAttribute('type', 'hidden');
	criarContagem.setAttribute('type', 'text');
	criarContagem.setAttribute('value', criou);
	criarContagem.setAttribute('name', criou);

	criou = criou + 1;
	criarElemento.setAttribute('type', 'submit');
	criarElemento.setAttribute('value', 'submit');


	taskLabel.setAttribute('for', description);
	taskLabel.appendChild(taskDescriptionNode);

	taskContainer.classList.add('task-item');
	taskContainer.appendChild(newTask);
	taskContainer.appendChild(taskLabel);

    taskSubmit.classList.add('task-submit');
	taskSubmit.appendChild(criarElemento);

	taskList.appendChild(taskContainer);
	taskList.appendChild(taskSubmit);

	};
}


