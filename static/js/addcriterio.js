const form = document.getElementById('task-criterio');
const taskList = document.getElementById('linha');
//const inputtype = document.getElementById('inputhidden');
var criou = 6;
var criado = 0;


form.onsubmit = function (e) {

	e.preventDefault();
	const inputField4 = document.getElementById('task-icriterio');
	addTask4(inputField.value);
	form.reset();
};


function addTask4(description) {
const taskContainer = document.createElement('div');
const newTask2 = document.createElement('input');
newTask2.setAttribute('type', 'text');
taskContainer.setAttribute('class', 'text-center mt-2');
if (criou >= 11){
newTask2.setAttribute('type', 'hidden');
};
newTask2.setAttribute('name', criou);
newTask2.setAttribute('id', description);
newTask2.setAttribute('value', description);
newTask2.setAttribute('class', 'form-control mt-2');
newTask2.setAttribute('value', description);

taskContainer.classList.add('criterios');
taskContainer.appendChild(newTask2);
taskListc.appendChild(taskContainer);
};