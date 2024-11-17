import { useQuery } from "react-query";
import { loginUser } from "../../api/auth.js";

export const useLogin = (login, password, showErrorToast) => {
	const { data, isLoading, isSuccess, isError, error, refetch } = useQuery({
		queryKey: ["login"],
		queryFn: () => loginUser(login, password),
		select: data => data.data,
		retry: false,
		enabled: false,
		onSuccess: () => {
			window.location.href = "/main";
		},
		onError: () => {
			showErrorToast("Что-то пошло не так...");
		},
	});

	return {
		loginData: data,
		loginIsLoading: isLoading,
		loginIsSuccess: isSuccess,
		loginIsError: isError,
		loginError: error,
		loginRefetch: refetch,
	};
};
