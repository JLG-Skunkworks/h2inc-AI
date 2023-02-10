import h2inc_AI as h2inc

if __name__ == "__main__":
    ai = h2inc.H2INC_AI("H2INC_AI")
    print(ai.getVersion(), ai.getCopyright(), ai.getAuthor(), ai.getContact(), sep = " - ")