#include <Python.h>


/**
 * print_python_list_info - print some basic information about Python lists
 * @p: pointer to PyObject
 * Return: no return
 */

void print_python_list_info(PyObject *p)
{
	long int length;
	int i;
	PyListObject *l_obj;

	length = PyList_Size(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < length; i++)
		printf("Element %i: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
