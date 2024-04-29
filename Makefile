RED := \033[31m
GREEN := \033[32m
RESET := \033[0m

all: venv install

venv:
	@echo "$(GREEN)creating virtual environnement...$(RESET)"
	@python -m venv virtualEnv
	@echo "$(GREEN)virtual environnement created$(RESET)"

install:
	@echo "$(GREEN)installing dependencies..."
	@. virtualEnv/bin/activate && pip install -r requirements.txt
	@echo "dependencies installed$(RESET)"

clean:
	@echo "$(RED)removing virtual environnement...$(RESET)"
	@rm -rf virtualEnv
	@echo "$(RED)virtual environnement removed$(RESET)	"

.PHONY: all venv install clean