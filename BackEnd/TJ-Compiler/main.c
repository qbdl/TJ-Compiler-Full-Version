#include"chibi.h"

// Returns the contents of a given file.
static char *read_file(char *path) 
{
  // Open and read the file.
  FILE *fp = fopen(path, "r");
  if (!fp)
    error("cannot open %s: %s", path, strerror(errno));

  int filemax = 10 * 1024 * 1024;
  char *buf = malloc(filemax);
  int size = fread(buf, 1, filemax - 2, fp);
  if (!feof(fp))
    error("%s: file too large");

  // Make sure that the string ends with "\n\0".
  if (size == 0 || buf[size - 1] != '\n')
    buf[size++] = '\n';
  buf[size] = '\0';
  return buf;
}


int align_to(int n,int align)
{
    return (n+align-1)&~(align-1);
}

int main(int argc,char **argv)
{
    if(argc!=2)
        error("%s: invalid number of arguments",argv[0]);

    // Tokenize and parse.
    filename = argv[1];
    user_input = read_file(argv[1]);
    token=tokenize();
    //从根节点往下进行汇编代码生成
    Program *prog = program();//调用顶部（内部自动完成AST树的生成）

    // Assign offsets to local variables.(暂时是单函数)
    for(Function *fn=prog->fns;fn;fn=fn->next){
        int offset = 0;
        for (VarList *vl = fn->locals; vl; vl = vl->next) {
            Var *var = vl->var;
            offset += var->ty->size;
            var->offset = offset;
        }
        fn->stack_size = align_to(offset,8);
    }
    
    // Traverse the AST to emit assembly.
    codegen(prog);

    return 0;
}