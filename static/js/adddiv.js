/*
var currentNumberWrapper = document.getElementById('currentNumber')
var currentNumber = 0;


function increment() {

        currentNumber = currentNumber + 1;
        currentNumberWrapper.innerHTML = currentNumber;

}
function decrement() {

        currentNumber = currentNumber - 1;
        currentNumberWrapper.innerHTML = currentNumber;

} */




const form = document.getElementById('task-form');
const taskList = document.getElementById('linha');
const inputtype = document.getElementById('inputhidden');
var criou = 0;
var criado = 0;
var ncontagem = 5;


form.onsubmit = function (e) {

	e.preventDefault();
	const inputField = document.getElementById('task-input');
	const inputField2 = document.getElementById('task-email');
	const inputField3 = document.getElementById('task-instituicao');
	const inputField4 = document.getElementById('task-icriterio');
	addTask4(inputField4.value);
	addTask(inputField.value);
	addTask2(inputField2.value);
	addTask3(inputField3.value);
	form.reset();
};


function addTask2(description) {
const taskContainer = document.createElement('div');
const newTask2 = document.createElement('input');
newTask2.setAttribute('type', 'text');
taskContainer.setAttribute('class', 'text-center mt-2');
if (criou >= 4){
newTask2.setAttribute('type', 'hidden');
};
newTask2.setAttribute('name', 'email'+criou);
newTask2.setAttribute('id', description);
newTask2.setAttribute('value', description);
newTask2.setAttribute('class', 'form-control mt-2');
newTask2.setAttribute('value', description);

taskContainer.classList.add('autores');
taskContainer.appendChild(newTask2);
taskList.appendChild(taskContainer);
};

function addTask3(description) {
const taskContainer = document.createElement('div');
const newTask3 = document.createElement('input');
newTask3.setAttribute('type', 'text');
taskContainer.setAttribute('class', 'text-center mt-2');
if (criou >= 4){
newTask3.setAttribute('type', 'hidden');
};
newTask3.setAttribute('name', 'inst'+criou);
newTask3.setAttribute('id', description);
newTask3.setAttribute('value', description);
newTask3.setAttribute('class', 'form-control mt-2');
newTask3.setAttribute('value', description);

taskContainer.classList.add('autores');
taskContainer.appendChild(newTask3);
taskList.appendChild(taskContainer);
};


function addTask(description) {

	const taskContainer = document.createElement('div');
	const taskSubmit = document.createElement('div')
	const newTask = document.createElement('input');



	//const taskLabel = document.createElement('label');

	//editType = document.getElementById('inputhidden');
	criarContagem = document.getElementById('inputcontagem');

	if (criado < 1) {
        criarElemento = document.createElement('input');
        criado = criado + 1;
	};



	const taskDescriptionNode = document.createTextNode('Autor:');
    if (criou <= 3){
    newTask.setAttribute('type', 'text');


    };

	if (criou >= 4){
	newTask.setAttribute('type', 'hidden');


	};
	newTask.setAttribute('name', criou);

	newTask.setAttribute('id', description);
	newTask.setAttribute('value', description);




	newTask.setAttribute('class', 'form-control mt-2');



	taskContainer.setAttribute('class', 'text-center mt-4');
	if (criou >= 4){
	newTask.setAttribute('value', '');
	};
	newTask.setAttribute('value', description);



	//editType.setAttribute('type', 'hidden');
	//criarContagem.setAttribute('type', 'text');
	criarContagem.setAttribute('value', criou);
	criarContagem.setAttribute('name', 'contagem');
	criou = criou + 1;
	//criarElemento.setAttribute('type', 'submit');
	//criarElemento.setAttribute('value', 'submit');
	//taskLabel.setAttribute('for', description);
	//taskLabel.setAttribute('class', 'mt-2 text-center');
	//taskLabel.appendChild(taskDescriptionNode);
	taskContainer.classList.add('autores');
	//taskContainer.appendChild(taskLabel);
	taskContainer.appendChild(newTask);
    //taskSubmit.classList.add('task-submit');
	//taskSubmit.appendChild(criarElemento);

	taskList.appendChild(taskContainer);
	taskList.appendChild(taskSubmit);

};

function addTask4(description) {

cCriterio = document.getElementById('ccriterios');
const taskContainer = document.createElement('div');
const newTask4 = document.createElement('input');
newTask4.setAttribute('type', 'text');
taskContainer.setAttribute('class', 'text-center');
criarContagem = document.getElementById('inputcontagem');
tacriado = ncontagem + 1;
cCriterio.setAttribute('value', tacriado);
if (criou >= 4){
newTask2.setAttribute('type', 'hidden');
cCriterio.setAttribute('value', 10);
};
newTask4.setAttribute('name', criou);
newTask4.setAttribute('id', description);
newTask4.setAttribute('value', description);
newTask4.setAttribute('class', 'form-control mt-2');
newTask4.setAttribute('value', description);

criarContagem.setAttribute('value', criou);
criarContagem.setAttribute('name', 'contagem');
criou = criou + 1;
ncontagem = ncontagem + 1;

taskContainer.classList.add('criterios');
taskContainer.appendChild(newTask4);
taskList.appendChild(taskContainer);

};






