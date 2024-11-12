# Pandey - UserBot
# Copyright (C) 2021-2023 TeamPandey
# This file is a part of < https://github.com/TeamPandey/Pandey/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/TeamPandey/Pandey/blob/main/LICENSE/>.

FROM theteamPragyan/Pragyan:main

# set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/TeamPandey"

# start the bot.
CMD ["bash", "startup"]
