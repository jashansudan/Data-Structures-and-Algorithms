class GapBuffer{

	char[] buffer;
	int gapStart;
	int gapEnd;

	public GapBuffer(int c){
		buffer = new char[c];
		gapStart = 0;
		gapEnd = c - 1;
	}

	public void insert(char c, int insert){
		if (gapStart > insert - 1){
			moveDown(gapStart - insert - 1);
		}
		else if (gapStart < insert - 1){
			moveUp(insert - 1 - gapStart);
		}
		buffer[gapStart] = c;
		gapStart++;
	}

	public void moveDown(int n){
		while (n > 0){
			buffer[gapEnd] = buffer[gapStart - 1];
			buffer[gapStart -1] = '\u0000';
			gapEnd --;
			gapStart--;
			n--;
		}
	}

	public void moveUp(int n){
		while (n > 0){
			buffer[gapStart] = buffer[gapEnd + 1];
			buffer[gapEnd + 1] = '\u0000';
			gapStart++;
			gapEnd++;
			n--;
		}
	}
	
	public void show(){
		for (int i = 0; i < buffer.length; i++){
			System.out.print(buffer[i]);
		}
		System.out.println(gapStart + " " + gapEnd);
	}

}