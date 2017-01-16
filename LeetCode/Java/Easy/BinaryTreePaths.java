package Easy;

import java.util.*;

public class BinaryTreePaths {

	public void main(String[] args) {

	}
	
	public List<String> binaryTreePaths(TreeNode root){
		List<String> answer = new ArrayList<String>();
		if (root != null){
			searchTree(root, "", answer);
		}
		return answer;
	}
	
	public void searchTree(TreeNode root, String path, List<String> answer){
		if (root.left == null && root.right == null){
			answer.add(path + root.val);
		}
		if (root.left != null){
			searchTree(root.left, path + root.val + "->", answer);
		}
		if (root.right != null){
			searchTree(root.right, path + root.val + "->", answer);
		}
	}

}
