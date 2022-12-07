
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
const taskList = document.getElementById('linha');
const inputtype = document.getElementById('inputhidden');
var criou = 0;
var criado = 0;


form.onsubmit = function (e) {

	e.preventDefault();
	const inputField = document.getElementById('task-input');
	addTask(inputField.value);
	form.reset();
};

function addTask(description) {


	const taskContainer = document.createElement('div');
	const taskSubmit = document.createElement('div')
	const newTask = document.createElement('input');

	//const taskLabel = document.createElement('label');

	editType = document.getElementById('inputhidden');
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
	taskContainer.setAttribute('class', 'text-center')
	if (criou >= 4){
	newTask.setAttribute('value', '');
	};
	newTask.setAttribute('value', description);
	editType.setAttribute('type', 'hidden');
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



}


