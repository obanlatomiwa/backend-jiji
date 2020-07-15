const TOKEN_KEY = 'user_token';
const tokenService = {
    getToken(){
        return localStorage.getItem(TOKEN_KEY)
    }
}

export {tokenService};