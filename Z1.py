import logging

# Создаем логгер
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем обработчик для логов уровня DEBUG и INFO
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)  # Устанавливаем уровень для обработчика

# Создаем обработчик для логов уровня WARNING и выше
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)  # Устанавливаем уровень для обработчика

# Создаем форматтер и применяем его к обработчикам
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Примеры логирования
logger.debug('Это сообщение уровня DEBUG')
logger.info('Это сообщение уровня INFO')
logger.warning('Это сообщение уровня WARNING')
logger.error('Это сообщение уровня ERROR')
logger.critical('Это сообщение уровня CRITICAL')

