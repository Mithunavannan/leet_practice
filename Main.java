class Test{
    public int high(int a, int b){
        return a > b ? a : b;
    }
    public int high(int a, int b, int c){
        if(a > b && a > c)
            return a;
        return c;
    }
}