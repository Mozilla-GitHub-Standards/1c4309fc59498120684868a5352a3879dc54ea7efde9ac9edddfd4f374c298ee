FROM python:3.6-onbuild

# Extra python env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# add non-priviledged user
RUN adduser --uid 1000 --disabled-password --gecos '' --ingroup autodeploy --no-create-home autodeploy

# get latest version of kubectl
ENV KUBECTL_VER=$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)
ADD https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VER/bin/linux/amd64/kubectl /usr/local/bin/kubectl
RUN chmod +x /usr/local/bin/kubectl

CMD ["python3", "/usr/src/app/autodeploy.py"]
