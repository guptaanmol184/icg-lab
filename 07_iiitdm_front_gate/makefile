default:
	@echo "No targets specified."
%.cpp.out: %.cpp
	g++ -fopenmp -g -o $@ $<
%.c.out: %.c
	gcc -g -o $@ $< -lrt -lreadline
clean:
	rm -rf *.out
%.py.out: %.py
	cp $< $@
	chmod +x $@
%.sh.out: %.sh
	cp $< $@
	chmod +x $@
