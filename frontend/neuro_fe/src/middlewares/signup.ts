import { NextFetchEvent, NextRequest, NextResponse } from "next/server";
import { MiddlewareFactory } from "./types";
import { getApi } from "./api";

export const signupMiddleware: MiddlewareFactory = (next) => {
	return async (request: NextRequest, _next: NextFetchEvent) => {
		if (request.nextUrl.pathname === "/api/signup") {
			const res = await fetch(`${getApi()}/api/user/create_user/`, {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: await request.text(),
			});

			if (res.status === 200) {
				return NextResponse.json(await res.json());
			};

			return new NextResponse(new Blob(), {status: 500});
		}

		return next(request, _next);
	};
};
