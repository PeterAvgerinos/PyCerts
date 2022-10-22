const int *array;
for (int i=0; i<5; i++) { 
    array[i] = i;
}
for (int i=0; i<1000; i++) { 
    array[i] = array[i]*8;
}
