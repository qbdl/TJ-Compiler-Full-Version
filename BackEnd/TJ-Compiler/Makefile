CFLAGS=-std=c11 -g -fno-common
SRCS=$(wildcard *.c)
OBJS=$(SRCS:.c=.o)

chibicc: $(OBJS)
	$(CC) -o $@ $(OBJS) $(LDFLAGS)

$(OBJS):chibi.h

test: chibicc
	./chibicc tests > tmp.s
	gcc -static -o tmp tmp.s
	./tmp

another_test: chibicc
	./chibicc my_test > tmp_my_test.s
	gcc -static -o tmp_my_test tmp_my_test.s
	@echo "Running my_test..."
	./tmp_my_test
	@echo "my_test finished with exit code $$?"

input_test:chibicc
	@./chibicc code_file > targetCode.s
	@gcc -static -o targetCode targetCode.s
	@./targetCode

clean:
	rm -f chibicc *.o *~ tmp* code_file code_file.s targetCode.s

.PHONY: test clean another_test input_test