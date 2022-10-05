/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) {
            TreeNode* head = new TreeNode(val);
            head->left = root;
            return head;
        }
        int current_depth = 1;
        queue<TreeNode*> que;
        que.push(root);
        while (!que.empty()) {
            int n = que.size();
            if (current_depth == depth-1) {
                for (int i=0; i < n; i++){
                    TreeNode* current = que.front();
                    que.pop();
                    TreeNode* currentRight = current->right;
                    TreeNode* currentLeft = current->left;
                    TreeNode* newLeft = new TreeNode(val);
                    TreeNode* newRight = new TreeNode(val);
                    current->left = newLeft;
                    current->right = newRight;
                    newLeft->left = currentLeft;
                    newRight->right = currentRight;
                }
                break;
            }
            for (int i=0; i < n; i++){
                TreeNode* current = que.front();
                que.pop();
                if (current->left){
                    que.push(current->left);
                }
                if (current->right){
                    que.push(current->right);
                }
            }
            
            current_depth++;
            
        }
        return root;
    }
};