next:
	git checkout `git log --reverse --ancestry-path HEAD..master | head -n 1 | cut -d \  -f 2`
begin:
	git checkout 43412ac7a84bd29078a021c868e80f3ed15e6676
