// /src/hooks/useAuth.tsx
import React, { useState, createContext, useContext, useEffect } from "react";

// Create the context 
const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
   // Store boolean to indicate whether a user is authenticated (default false)
   const [authed, setAuthed] = useState(false);
   // Store new value to indicate the call has not finished (default true)
   const [loading, setLoading] = useState(true);

   const signup = async (email, password) => {
      const signUpResult = await asyncServerSignUp(email, password);
      if (signUpResult) {
         setAuthed(true);
      }
   }

   const login = async (email, password) => {
      const loginResult = await asyncServerLogin(email, password);
      if (loginResult) {
         setAuthed(true);
      }
   }

   // const loginGoogle = async (googleData) => {
   //    // log in to the server
   //    const loginResult = await asyncServerGoogleLogin(googleData.tokenId);
   //    // if successful, set authed var to true
   //    if (loginResult) {
   //       setAuthed(true);
   //    }
   // }

   const logout = async () => {
      const logoutResult = await asyncServerLogout();
      if (logoutResult) {
         setAuthed(false);
      }
   }

   const asyncServerSignUp = async (email, password) => {
      const resp = await fetch('/api/register', {
         method: 'POST',
         body: JSON.stringify({
             email: email,
             password: password
         }),
         headers: {
             'Content-Type': 'application/json'
         }
     });
     const data = await resp.json();
     if (data) {
         return data.success;
     } else {
        return false;
     }
   }

   const asyncServerLogin = async (email, password) => {
      const resp = await fetch('/api/login', {
         method: 'POST',
         body: JSON.stringify({
             email: email,
             password: password
         }),
         headers: {
             'Content-Type': 'application/json'
         }
     });
     const data = await resp.json();
     if (data) {
         return data.success;
     } else {
        return false;
     }
   }

   // const asyncServerGoogleLogin = async (googleTokenId) => {
   //    const resp = await fetch('/api/login', {
   //       method: 'POST',
   //       body: JSON.stringify({
   //           token: googleTokenId
   //       }),
   //       headers: {
   //           'Content-Type': 'application/json'
   //       }
   //   });
   //   const data = await resp.json();
   //   if (data) {
   //       return data.logged_in;
   //   } else {
   //      return false;
   //   }
   // }

   const asyncServerLogout = async () => {
      const resp = await fetch('/api/logout');
      const data = await resp.json();
      if (data) {
         return data.logged_out;
      } else {
         return false;
      }
   }

   // Runs once when the component first mounts
   useEffect(() => {
      asyncServerAuthCheck().then((authenticatedUser) => {
         if (authenticatedUser) {
            setAuthed(true);
            setLoading(false);
         } else {
            setAuthed(false);
            setLoading(false);
         }
      });
   }, []);

   // Verify authentication with server
   const asyncServerAuthCheck = async () => {
      const resp = await fetch('/api/auth');
      const data = await resp.json();
      if (data) {
         return data.authenticated;
      } else {
         return false;
      }
   }

   return (
      // Expose the new `loading` value so we can consume it in `App.tsx`
      <AuthContext.Provider
         value={{ authed, setAuthed, signup, login, logout, loading }}
      >
         {children}
      </AuthContext.Provider>
   );
}

// Finally creating the custom hook 
export const useAuth = () => useContext(AuthContext);