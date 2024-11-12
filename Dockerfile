# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# Please read the GNU Affero General Public License in <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

# Use the official TeamUltroid image as base
FROM theteamultroid/ultroid:main

# Set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy the installer script
COPY installer.sh /root/

# Run the installer script
RUN bash /root/installer.sh

# Create the pyPandey directory
RUN mkdir -p /root/pyPandey

# Copy project files into the newly created directory
COPY . /root/pyPandey

# Change working directory to pyPandey
WORKDIR /root/pyPandey

# Install dependencies (if there's a requirements.txt in the copied files)
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

# Start the bot
CMD ["bash", "startup"]
